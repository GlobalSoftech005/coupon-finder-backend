# backend.py (Flask)
from flask import Flask, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

SHOPIFY_STORE = os.getenv("SHOPIFY_STORE")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_VERSION = os.getenv("API_VERSION")


@app.route('/api/discount-usage/<code>')
def get_discount_usage(code):
    url = f"https://{SHOPIFY_STORE}/admin/api/{API_VERSION}/orders.json?discount_code={code}"
    headers = {
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return jsonify({
        "count": len(data.get("orders", [])),
        "orders": data.get("orders", [])
    })

if __name__ == '__main__':
    app.run(debug=True)
