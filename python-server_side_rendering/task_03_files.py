from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Product Loader! Use /display?source=json or /display?source=csv"

@app.route('/display')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_msg = None

    # 1. Mənbəni yoxla
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. JSON oxuma məntiqi
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found")

    # 3. CSV oxuma məntiqi
    elif source == 'csv':
        try:
            with open('products.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # ID-ni müqayisə üçün int-ə çeviririk
                    row['id'] = int(row['id'])
                    products.append(row)
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found")

    # 4. ID-yə görə filtrləmə
    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
