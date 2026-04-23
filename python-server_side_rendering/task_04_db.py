from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# SQL-dən məlumatı oxumaq üçün köməkçi funksiya
def fetch_from_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Bu, nəticəni lüğətə bənzər formatda qaytarır
        cursor = conn.cursor()

        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            rows = cursor.fetchall()
        else:
            cursor.execute('SELECT * FROM Products')
            rows = cursor.fetchall()

        conn.close()
        return [dict(row) for row in rows], None
    except sqlite3.Error as e:
        return [], f"Database error: {e}"

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    # 1. Mənbəni yoxla
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. JSON məntiqi
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            error = "JSON file not found"

    # 3. CSV məntiqi
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products = [row for row in reader]
                for p in products: p['id'] = int(p['id']) # ID-ni rəqəmə çevir
        except FileNotFoundError:
            error = "CSV file not found"

    # 4. SQL məntiqi
    elif source == 'sql':
        products, error = fetch_from_sql(product_id)
        # SQL filtrləməni artıq query-də etdiyimiz üçün aşağıdakı filtrə ehtiyac yoxdur
        return render_template('product_display.html', products=products, error=error)

    # 5. JSON və CSV üçün ID filtrləmə (SQL artıq daxildə həll edib)
    if product_id is not None and source != 'sql':
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
