import json
from flask import Flask, render_template

app = Flask(__name__)

# Əvvəlki route-lar (home, about, contact) buradadır...

@app.route('/items')
def items():
    # JSON faylından məlumatı oxuyuruq
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []

    # Məlumatı şablona göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
