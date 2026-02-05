#!/usr/bin/env python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_items():
    """Read items.json and return the list under the 'items' key."""
    filepath = os.path.join(os.path.dirname(__file__), "items.json")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("items", [])
        # Ensure it's always a list
        return items if isinstance(items, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        # If file missing or broken JSON, treat as no items
        return []

@app.route("/items")
def items_page():
    items = load_items()
    return render_template("items.html", items=items)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

