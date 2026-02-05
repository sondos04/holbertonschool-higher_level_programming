#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")
DB_PATH = os.path.join(BASE_DIR, "products.db")


def read_products_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else []


def read_products_csv():
    products = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]) if row.get("id") else 0,
                "name": row.get("name", ""),
                "category": row.get("category", ""),
                "price": float(row["price"]) if row.get("price") else 0.0,
            })
    return products


def read_products_sql():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for r in rows:
        products.append({
            "id": r[0],
            "name": r[1],
            "category": r[2],
            "price": r[3],
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    raw_id = request.args.get("id")

    products_list = []
    error = None

    try:
        if source == "json":
            products_list = read_products_json()
        elif source == "csv":
            products_list = read_products_csv()
        elif source == "sql":
            products_list = read_products_sql()
        else:
            return render_template("product_display.html", error="Wrong source", products=[])
    except FileNotFoundError:
        products_list = []
    except json.JSONDecodeError:
        products_list = []
    except sqlite3.Error:
        return render_template("product_display.html", error="Database error", products=[])

    if raw_id is not None:
        try:
            wanted_id = int(raw_id)
        except ValueError:
            return render_template("product_display.html", error="Product not found", products=[])

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])
        products_list = filtered

    return render_template("product_display.html", error=error, products=products_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

