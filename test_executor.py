from executor.apply_changes import apply_changes, log_changes

# Example page data
page_data = {"url": "https://example.com", "title": "", "meta_description": "", "h1": ""}
backlog = [
    {"issue": "Missing <title>"},
    {"issue": "Missing meta description"},
    {"issue": "Missing <h1>"}
]

# Apply changes
changes = apply_changes(page_data, backlog)
log_changes(page_data["url"], changes)

# Print results
print("Applied changes:")
print(changes)