# planner/recommend.py

def prioritize_issues(issues):
    backlog = []

    for issue in issues:
        if "title" in issue.lower():
            backlog.append({
                "issue": issue,
                "impact": "High",
                "effort": "Low",
                "confidence": "High",
                "proposed_fix": "Add a descriptive <title> tag"
            })
        elif "meta" in issue.lower():
            backlog.append({
                "issue": issue,
                "impact": "Medium",
                "effort": "Low",
                "confidence": "High",
                "proposed_fix": "Add a meta description tag"
            })
        elif "h1" in issue.lower():
            backlog.append({
                "issue": issue,
                "impact": "Medium",
                "effort": "Low",
                "confidence": "High",
                "proposed_fix": "Add an <h1> heading on the page"
            })
    return backlog

# Quick test
if __name__ == "__main__":
    test_issues = ["Missing or empty <title>", "Missing or empty meta description"]
    backlog = prioritize_issues(test_issues)
    print(backlog)