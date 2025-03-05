from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from React

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/')
def home():
    return "Flask Backend is Running!"

if __name__ == '__main__':
    app.run(debug=True)
