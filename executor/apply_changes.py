# executor/apply_changes.py

import os
import json

def apply_changes(page_data, backlog):
    changes = []
    for task in backlog:
        if "title" in task["issue"].lower():
            # For demo, we just simulate the change
            new_title = "New Title"
            changes.append(f"Title would be updated to: '{new_title}'")
            page_data["title"] = new_title

        elif "meta" in task["issue"].lower():
            new_meta = "This is an example meta description."
            changes.append(f"Meta description would be updated to: '{new_meta}'")
            page_data["meta_description"] = new_meta

        elif "h1" in task["issue"].lower():
            new_h1 = "Example Heading"
            changes.append(f"H1 would be added: '{new_h1}'")
            page_data["h1"] = new_h1

    return changes

def log_changes(page_url, changes):
    os.makedirs("logs", exist_ok=True)
    log_entry = {"url": page_url, "changes": changes}
    with open("logs/changes.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")