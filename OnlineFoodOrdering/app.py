from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Online Food Ordering System"

@app.route("/menu")
def menu():
    return jsonify([
        {"id": 1, "name": "Pizza", "price": 150},
        {"id": 2, "name": "Burger", "price": 100}
    ])

@app.route("/order")
def order():
    return "Order placed successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)