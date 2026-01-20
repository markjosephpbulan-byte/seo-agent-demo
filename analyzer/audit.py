# analyzer/audit.py

def analyze_page(page_data):
    issues = []

    if not page_data.get("title") or page_data["title"].strip() == "":
        issues.append("Missing or empty <title>")

    if not page_data.get("meta_description") or page_data["meta_description"].strip() == "" or page_data["meta_description"] == "No meta description":
        issues.append("Missing or empty meta description")

    if not page_data.get("h1") or page_data["h1"].strip() == "" or page_data["h1"] == "No H1":
        issues.append("Missing or empty <h1>")

    return issues

# Test it
if __name__ == "__main__":
    # Example page data
    page = {
        "url": "https://example.com",
        "title": "Example Domain",
        "meta_description": "No meta description",
        "h1": "Example Domain"
    }

    result = analyze_page(page)
    print("SEO Issues found:", result)