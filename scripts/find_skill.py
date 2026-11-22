import argparse
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DEFAULT_INDEX_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "skills_index.json",
)


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
        term_score = 0
        if t == slug or t == name:
            term_score = max(term_score, 50)
        elif t in slug_tokens:
            term_score = max(term_score, 28)
        elif t in slug:
            term_score = max(term_score, 18)

        if re.search(r"\b" + re.escape(t) + r"\b", tags):
            term_score += 8
        elif t in tags:
            term_score += 4

        if re.search(r"\b" + re.escape(t) + r"\b", cat):
            term_score += 6

        if re.search(r"\b" + re.escape(t) + r"\b", desc):
            term_score += 8
        elif t in desc:
            term_score += 3

        if t in pack:
            term_score += 2

        if term_score > 0:
            matched_terms += 1
            score += term_score

    if len(terms) > 1 and matched_terms > 0:
        score += 18 * matched_terms
        if matched_terms == len(terms):
            score += 25
    return score


def main():
    parser = argparse.ArgumentParser(description="Search globally installed Antigravity skills.")
    parser.add_argument("query", nargs="*", help="Keywords or skill name to search for")
    parser.add_argument("--pack", help="Filter by plugin pack name (e.g. skills-web-frontend)")
    parser.add_argument("--top", type=int, default=8, help="Max results to return (default: 8)")
    parser.add_argument("--list-packs", action="store_true", help="List all packs and skill counts")
    parser.add_argument("--info", help="Show details and path for an exact skill slug")
    parser.add_argument("--index", default=DEFAULT_INDEX_PATH, help=argparse.SUPPRESS)
    args = parser.parse_args()

    items = load_index(args.index)

    if args.list_packs:
        counts = {}
        for it in items:
            p = it.get("pack", "unknown")
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
    pool = [it for it in items if not args.pack or it.get("pack") == args.pack]

    scored = []
    for it in pool:
        s = score_skill(it, terms, raw_query)
        if s > 0:
            scored.append((s, it))

    scored.sort(key=lambda x: (-x[0], x[1].get("slug", "")))
    if not scored:
        print(f"No matches for '{raw_query}'. Try broader keywords or --list-packs.")
        return

    for s, it in scored[: max(1, args.top)]:
        print(f"[{it['slug']}] (pack: {it['pack']}, score: {s})")
        print(f"  desc: {it['desc'][:200]}")
        print(f"  path: {it['path']}")


if __name__ == "__main__":
    main()
