#!/usr/bin/env python3
"""Search the memory repo for keywords across all files."""
import os
import sys
import re
from pathlib import Path

REPO_ROOT = Path.home() / "k2-6-memory"
SEARCH_DIRS = ["docs", "runbooks", "goals", "logs", "schemas"]

def search(keyword, case_sensitive=False):
    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(re.escape(keyword), flags)
    
    results = []
    for dirname in SEARCH_DIRS:
        dirpath = REPO_ROOT / dirname
        if not dirpath.exists():
            continue
        for filepath in dirpath.rglob("*"):
            if filepath.is_file() and filepath.suffix in (".md", ".yaml", ".yml", ".txt", ".sh", ".py"):
                try:
                    content = filepath.read_text(encoding="utf-8")
                    matches = list(pattern.finditer(content))
                    if matches:
                        # Show first match context
                        m = matches[0]
                        start = max(0, m.start() - 60)
                        end = min(len(content), m.end() + 60)
                        context = content[start:end].replace("\n", " ")
                        results.append({
                            "file": str(filepath.relative_to(REPO_ROOT)),
                            "matches": len(matches),
                            "context": context
                        })
                except Exception:
                    continue
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <keyword>")
        sys.exit(1)
    
    keyword = sys.argv[1]
    results = search(keyword)
    
    if not results:
        print(f"No matches for '{keyword}'")
        sys.exit(0)
    
    print(f"Found {len(results)} files matching '{keyword}':\n")
    for r in results:
        print(f"  {r['file']} ({r['matches']} matches)")
        print(f"    ... {r['context']} ...")
        print()
