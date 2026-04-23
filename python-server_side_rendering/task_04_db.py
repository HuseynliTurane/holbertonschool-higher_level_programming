import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    """SQLite verilənlər bazasını yaradır və ilkin məlumatları daxil edir."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Əgər cədvəl boşdursa, nümunə məlumatları əlavə et
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()

def fetch_from_sql(product_id=None):
    """SQLite-dan məlumatları oxuyur."""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id is not None:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')

        rows = cursor.fetchall()
        conn.close()
        # Row obyektlərini standart lüğətə (dict) çeviririk
        return [dict(row) for row in rows], None
    except sqlite3.Error as e:
        return [], f"Database error: {e}"

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    # 1. Mənbə yoxlaması
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. JSON Mənbəsi
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            error = "JSON file not found"

    # 3. CSV Mənbəsi
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products = [row for row in reader]
                # ID-ləri rəqəmə çevirmək (filtrasiya üçün)
                for p in products:
                    p['id'] = int(p['id'])
        except FileNotFoundError:
            error = "CSV file not found"

    # 4. SQL Mənbəsi
    elif source == 'sql':
        products, error = fetch_from_sql(product_id)
        # Əgər ID verilibsə və nəticə boşdursa -> Product not found
        if product_id is not None and not products and not error:
            error = "Product not found"
        return render_template('product_display.html', products=products, error=error)

    # 5. JSON və CSV üçün ID filtrləmə məntiqi
    if product_id is not None and not error:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    # Server başlamazdan əvvəl bazanın mövcudluğunu təmin edirik
    create_database()
    app.run(debug=True, port=5000)
