#!/usr/bin/env python3
"""
Cross-Agent Memory Scanner for Kimi K2.6.
Crawls inventory.yaml files from all 14 village memory repositories and builds
a local searchable catalog (JSON + Markdown summary).

Adapted from Gemini 3.5 Flash's scan_peers.py; adds:
- --stats mode for cross-repo distribution analysis
- searches all normalized fields, not just id/summary/cue
- writes a human-readable Markdown summary alongside JSON
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime

import urllib.request
import urllib.error
import yaml

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONSOLIDATED_JSON = os.path.join(VAULT_ROOT, "peers", "consolidated_inventory.json")
CONSOLIDATED_MD = os.path.join(VAULT_ROOT, "peers", "consolidated_inventory.md")

# 14 peer repos across #best and #rest
PEER_REPOS = [
    "gpt-5-5-memory-improvement",
    "claude-opus-4-7-memory",
    "gemini-3-5-flash-memory-vault",
    "gpt-5-2-memory-improvement",
    "opus-46-memory",
    "gpt-5-4-memory-kit",
    "claude-opus-memory",
    "memory-improvement",
    "haiku-memory-system",
    "gemini-3.1-pro-memory",
    "gpt-5-1-memory",
    "deepseek-v3.2-memory-system",
    "fortified-evidentiary-memory",
    "k2-6-memory",  # include self for completeness
]


def get_peer_repos(discover=False):
    repos = list(PEER_REPOS)
    if not discover:
        return repos

    discovered = []
    try:
        result = subprocess.run(
            [
                "gh",
                "repo",
                "list",
                "ai-village-agents",
                "--limit",
                "100",
                "--json",
                "name",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(result.stdout)
        if isinstance(data, list):
            for row in data:
                if not isinstance(row, dict):
                    continue
                name = row.get("name")
                if isinstance(name, str) and "memory" in name.lower():
                    discovered.append(name)
    except (subprocess.SubprocessError, json.JSONDecodeError, OSError) as e:
        print(f"[WARNING] Repo discovery failed ({e}); using hardcoded repos only.")
        print(
            f"[*] Repo discovery: hardcoded={len(PEER_REPOS)}, "
            "discovered=0, total_unique="
            f"{len(PEER_REPOS)}"
        )
        return repos

    seen = set(repos)
    added_count = 0
    for repo in discovered:
        if repo in seen:
            continue
        repos.append(repo)
        seen.add(repo)
        added_count += 1

    print(
        f"[*] Repo discovery: hardcoded={len(PEER_REPOS)}, "
        f"discovered={len(discovered)}, added={added_count}, total_unique={len(repos)}"
    )
    return repos


def format_val(val):
    if val is None:
        return ""
    if isinstance(val, (datetime,)):
        return val.isoformat()
    return str(val)


def fetch_inventory(repo):
    branches = ["main", "master"]
    for branch in branches:
        url = f"https://raw.githubusercontent.com/ai-village-agents/{repo}/{branch}/inventory.yaml"
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"},
            )
            with urllib.request.urlopen(req, timeout=15) as response:
                return response.read().decode("utf-8"), branch, url
        except urllib.error.URLError:
            continue
    return None, None, None


def normalize_items(raw_content, repo, branch):
    items = yaml.safe_load(raw_content)
    if items is None:
        return []
    if isinstance(items, dict) and "items" in items:
        items = items["items"]
    if not isinstance(items, list):
        return []

    normalized = []
    for item in items:
        if not isinstance(item, dict):
            continue
        path = format_val(item.get("path", item.get("file", "")))
        normalized.append({
            "id": format_val(item.get("id", "unknown")),
            "status": format_val(item.get("status", "unknown")),
            "kind": format_val(item.get("kind", "unknown")),
            "summary": format_val(item.get("summary", "")),
            "source_repo": repo,
            "last_verified": format_val(item.get("last_verified", "unknown")),
            "retrieval_cue": format_val(item.get("retrieval_cue", "")),
            "internal_memory_policy": format_val(item.get("internal_memory_policy", "")),
            "path": path,
            "url": f"https://github.com/ai-village-agents/{repo}/blob/{branch}/{path}",
        })
    return normalized


def scan_all(peer_repos=None):
    peer_repos = peer_repos or PEER_REPOS
    print("=" * 65)
    print("           CROSS-AGENT MEMORY INVENTORY CRAWLER")
    print("=" * 65)
    print(f"[*] Crawling {len(peer_repos)} peer repositories...\n")

    consolidated = []
    success_count = 0
    per_repo_counts = {}

    for repo in peer_repos:
        label = repo if repo != "k2-6-memory" else "k2-6-memory (self)"
        print(f"[*] Fetching: {label} ...", end="", flush=True)
        content, branch, url = fetch_inventory(repo)
        if not content:
            print(" [FAILED] (no inventory.yaml on main/master)")
            continue
        try:
            repo_items = normalize_items(content, repo, branch)
            if not repo_items:
                print(" [EMPTY] (no valid items)")
                continue
            consolidated.extend(repo_items)
            success_count += 1
            per_repo_counts[repo] = len(repo_items)
            print(f" [OK] ({len(repo_items)} items, branch '{branch}')")
        except Exception as e:
            print(f" [ERROR] ({e})")

    # Write JSON
    os.makedirs(os.path.dirname(CONSOLIDATED_JSON), exist_ok=True)
    with open(CONSOLIDATED_JSON, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)

    # Write Markdown summary
    with open(CONSOLIDATED_MD, "w", encoding="utf-8") as f:
        f.write("# Cross-Agent Consolidated Inventory\n\n")
        f.write(f"Generated: {datetime.utcnow().isoformat()}Z\n\n")
        f.write(f"**Success**: {success_count}/{len(peer_repos)} repos\n")
        f.write(f"**Total items**: {len(consolidated)}\n\n")
        f.write("## Per-Repo Counts\n\n")
        for repo, count in sorted(per_repo_counts.items()):
            f.write(f"- `{repo}`: {count} items\n")
        f.write("\n## All Items\n\n")
        for item in consolidated:
            f.write(f"### {item['id']} ({item['status']}) — {item['source_repo']}\n")
            f.write(f"- **Kind**: {item['kind']}\n")
            f.write(f"- **Summary**: {item['summary']}\n")
            f.write(f"- **Path**: `{item['path']}`\n")
            f.write(f"- **URL**: {item['url']}\n")
            f.write(f"- **Retrieval cue**: {item['retrieval_cue']}\n")
            f.write(f"- **Internal memory policy**: {item['internal_memory_policy']}\n\n")

    print("-" * 65)
    print(f"[SUCCESS] Scanned {success_count}/{len(peer_repos)} repos.")
    print(f"[SUCCESS] Total items: {len(consolidated)}.")
    print(f"[SUCCESS] JSON:  {CONSOLIDATED_JSON}")
    print(f"[SUCCESS] MD:    {CONSOLIDATED_MD}")
    print("=" * 65)
    return consolidated, per_repo_counts


def list_repos():
    print("Tracked peer memory repos:")
    for idx, repo in enumerate(PEER_REPOS, 1):
        print(f"  {idx:02d}. https://github.com/ai-village-agents/{repo}")


def search_index(query, discover=False):
    if discover or not os.path.exists(CONSOLIDATED_JSON):
        if discover:
            print("[*] --discover enabled; refreshing consolidated index before search...")
        else:
            print("[WARNING] No consolidated index found. Running scan first...")
        peer_repos = get_peer_repos(discover=True) if discover else PEER_REPOS
        scan_all(peer_repos=peer_repos)

    with open(CONSOLIDATED_JSON, "r", encoding="utf-8") as f:
        items = json.load(f)

    print(f"Searching cross-agent index for: '{query}'")
    print("-" * 65)

    try:
        rx = re.compile(query, re.IGNORECASE)
    except re.error as e:
        print(f"[ERROR] Invalid regex: {e}")
        sys.exit(1)

    matches = 0
    for item in items:
        haystack = " ".join(str(v) for v in item.values())
        if rx.search(haystack):
            matches += 1
            print(f"\n[{matches:02d}] {item['id']} ({item['kind']}) [{item['status']}]")
            print(f"     Repo:  {item['source_repo']}")
            print(f"     Sum:   {item['summary'][:100]}")
            print(f"     Cue:   {item['retrieval_cue'][:80]}")
            print(f"     URL:   {item['url']}")

    print("-" * 65)
    print(f"[*] Found {matches} matching items.")


def show_stats(discover=False):
    if discover or not os.path.exists(CONSOLIDATED_JSON):
        if discover:
            print("[*] --discover enabled; refreshing consolidated index before stats...")
        else:
            print("[WARNING] No consolidated index found. Running scan first...")
        peer_repos = get_peer_repos(discover=True) if discover else PEER_REPOS
        scan_all(peer_repos=peer_repos)

    with open(CONSOLIDATED_JSON, "r", encoding="utf-8") as f:
        items = json.load(f)

    repo_counts = Counter(item["source_repo"] for item in items)
    status_counts = Counter(item["status"] for item in items)
    kind_counts = Counter(item["kind"] for item in items)
    policy_counts = Counter(item["internal_memory_policy"] for item in items if item["internal_memory_policy"])

    print("=" * 65)
    print("           CROSS-AGENT INVENTORY STATISTICS")
    print("=" * 65)
    print(f"\nTotal items: {len(items)}")
    print(f"Repos represented: {len(repo_counts)}")

    print("\n--- Per-Repo ---")
    for repo, count in repo_counts.most_common():
        print(f"  {repo:40s} {count:3d}")

    print("\n--- Status Distribution ---")
    for status, count in status_counts.most_common():
        print(f"  {status:20s} {count:3d}")

    print("\n--- Kind Distribution ---")
    for kind, count in kind_counts.most_common():
        print(f"  {kind:20s} {count:3d}")

    if policy_counts:
        print("\n--- Internal Memory Policy Distribution ---")
        for policy, count in policy_counts.most_common():
            print(f"  {policy:20s} {count:3d}")

    print("=" * 65)


def main():
    parser = argparse.ArgumentParser(description="Cross-Agent Memory Scanner")
    parser.add_argument("--scan", "-s", action="store_true", help="Scan all peer inventories")
    parser.add_argument("--list", "-l", action="store_true", help="List tracked repos")
    parser.add_argument("--search", "-q", type=str, metavar="QUERY", help="Regex search across all fields")
    parser.add_argument("--stats", action="store_true", help="Show distribution stats")
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Discover additional memory repos via 'gh repo list ai-village-agents'",
    )
    args = parser.parse_args()

    if args.list:
        list_repos()
    elif args.search:
        search_index(args.search, discover=args.discover)
    elif args.stats:
        show_stats(discover=args.discover)
    else:
        scan_all(peer_repos=get_peer_repos(discover=args.discover))


if __name__ == "__main__":
    main()
