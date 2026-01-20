# main.py

from crawler.crawl import extract_page_data
from analyzer.audit import analyze_page
from planner.recommend import prioritize_issues
from executor.apply_changes import apply_changes, log_changes

def main():
    print("=== SEO Agent Demo ===")
    url = input("Enter a URL to audit: ")

    # Step 1: Crawl
    page_data = extract_page_data(url)
    print("\nCrawled Page Data:")
    print(page_data)

    # 🚧 GUARDRAIL: stop if crawl failed
    if page_data is None:
        print("\n❌ Crawl failed. Stopping safely.")
        return

    # Step 2: Analyze
    issues = analyze_page(page_data)
    print("\nSEO Issues Found:")
    print(issues)

    if not issues:
        print("\nNo issues detected. Page looks good!")
        return

    # Step 3: Prioritize / Recommendation
    backlog = prioritize_issues(issues)
    print("\nRecommendation Backlog:")
    for task in backlog:
        print(f"- {task['issue']} | Impact: {task['impact']} | Effort: {task['effort']} | Proposed fix: {task['proposed_fix']}")

    # Step 4: Apply safe changes
    changes = apply_changes(page_data, backlog)
    log_changes(url, changes)
    print("\nApplied Safe Changes:")
    for change in changes:
        print(f"- {change}")

    print("\nDemo Complete! Changes have been logged in logs/changes.json")

if __name__ == "__main__":
    main()