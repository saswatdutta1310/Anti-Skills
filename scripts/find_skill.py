import argparse
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INDEX_PATH = os.path.join(REPO_ROOT, "data", "skills_index.json")


def load_index(index_path=DEFAULT_INDEX_PATH):
    with open(index_path, "r", encoding="utf-8") as f:
        return json.load(f)


def score_skill(item, terms, raw_query):
    slug = item.get("slug", "").lower()
    name = item.get("name", "").lower()
    desc = item.get("desc", "").lower()
    cat = item.get("category", "").lower()
    tags = " ".join(item.get("tags", [])).lower()
    pack = item.get("pack", "").lower()

    score = 0
    if raw_query == slug or raw_query == name:
        score += 120
    elif raw_query in slug or raw_query in name:
        score += 45

    matched_terms = 0
    slug_tokens = set(re.split(r"[-_]+", slug))
    for t in terms:
        if not t:
            continue
        hit = False
        if t in slug_tokens:
            score += 40
            hit = True
        elif t in slug or t in name:
            score += 25
            hit = True
        if t in cat:
            score += 15
            hit = True
        if t in desc:
            score += 10
            hit = True
        if t in tags or t in pack:
            score += 8
            hit = True
        if hit:
            matched_terms += 1

    if len(terms) > 1 and matched_terms == len(terms):
        score += 35

    return score


def main():
    parser = argparse.ArgumentParser(description="Search Anti-Skills catalog.")
    parser.add_argument("query", nargs="*", help="Keywords or skill name to search for")
    parser.add_argument("--category", "--pack", dest="cat", help="Filter by category or pack name")
    parser.add_argument("--top", type=int, default=8, help="Max results to return (default: 8)")
    parser.add_argument("--list-categories", "--list-packs", action="store_true", help="List all categories and skill counts")
    parser.add_argument("--info", help="Show details and path for an exact skill slug")
    parser.add_argument("--index", default=DEFAULT_INDEX_PATH, help=argparse.SUPPRESS)
    args = parser.parse_args()

    items = load_index(args.index)

    if args.list_categories:
        counts = {}
        for it in items:
            p = it.get("category", it.get("pack", "unknown"))
            counts[p] = counts.get(p, 0) + 1
        for p, c in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"{p:34s} {c:4d}")
        print(f"Total indexed skills: {len(items)}")
        return

    if args.info:
        target = args.info.strip().lower()
        matches = [it for it in items if it.get("slug", "").lower() == target or it.get("name", "").lower() == target]
        if not matches:
            print(f"No exact skill found for '{args.info}'.")
            sys.exit(1)
        for it in matches:
            print(json.dumps(it, indent=2, ensure_ascii=False))
        return

    raw_query = " ".join(args.query).strip().lower()
    if not raw_query:
        parser.print_help()
        return

    terms = [t for t in re.split(r"[\s,/+]+", raw_query) if len(t) >= 2 or t.isalnum()]
    pool = [it for it in items if not args.cat or it.get("category") == args.cat or it.get("pack") == args.cat]

    scored = []
    for it in pool:
        s = score_skill(it, terms, raw_query)
        if s > 0:
            scored.append((s, it))

    scored.sort(key=lambda x: (-x[0], x[1].get("slug", "")))
    if not scored:
        print(f"No matches for '{raw_query}'. Try broader keywords or --list-categories.")
        return

    for s, it in scored[: max(1, args.top)]:
        cat = it.get("category", it.get("pack", "general"))
        rel_path = it.get("repo_path")
        if rel_path and os.path.exists(os.path.join(REPO_ROOT, rel_path)):
            display_path = rel_path
        else:
            display_path = it.get("path", "")
        print(f"[{it['slug']}] (category: {cat}, score: {s})")
        print(f"  desc: {it['desc'][:200]}")
        print(f"  path: {display_path}")


if __name__ == "__main__":
    main()
