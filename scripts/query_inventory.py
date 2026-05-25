#!/usr/bin/env python3
import sys, yaml, os

REPO = os.path.expanduser("~/k2-6-memory")
INV = os.path.join(REPO, "inventory.yaml")

def query(q):
    tokens = q.lower().split()
    with open(INV) as f:
        data = yaml.safe_load(f)
    items = data.get("items", [])
    matches = []
    for item in items:
        text = " ".join(str(v) for v in item.values() if v is not None).lower()
        if all(t in text for t in tokens):
            matches.append(item)
    return matches

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <query>")
        sys.exit(1)
    q = sys.argv[1]
    matches = query(q)
    print("Found " + str(len(matches)) + " item(s) for '" + q + "':")
    for m in matches:
        i = m.get("id", "?")
        s = m.get("status", "?")
        k = m.get("kind", "?")
        su = m.get("summary", "")
        print("  - " + i + " [" + s + "] " + k + ": " + su)
        if m.get("path"):
            print("    path: " + m["path"])
        print()
