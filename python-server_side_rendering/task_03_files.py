#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")


def read_products_json():
    """Return a list of product dicts from products.json."""
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else []


def read_products_csv():
    """Return a list of product dicts from products.csv."""
    products = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert types to match JSON style
            product = {
                "id": int(row.get("id", 0)) if row.get("id") else 0,
                "name": row.get("name", ""),
                "category": row.get("category", ""),
                "price": float(row.get("price", 0)) if row.get("price") else 0.0,
            }
            products.append(product)
    return products


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    raw_id = request.args.get("id")  # optional
    products_list = []
    error = None

    # Validate source and load data
    if source == "json":
        try:
            products_list = read_products_json()
        except (FileNotFoundError, json.JSONDecodeError):
            products_list = []
    elif source == "csv":
        try:
            products_list = read_products_csv()
        except FileNotFoundError:
            products_list = []
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error, products=[])

    # Filter by id if provided
    if raw_id is not None:
        try:
            wanted_id = int(raw_id)
        except ValueError:
            # Treat invalid id as not found (keeps behavior simple)
            return render_template(
                "product_display.html", error="Product not found", products=[]
            )

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", error=error, products=[])
        products_list = filtered

    return render_template("product_display.html", products=products_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

