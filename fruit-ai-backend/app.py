from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS

faqs = [{"id": 1, "question": "What is Apple?", "answer": "An apple is a fruit."}]

@app.route('/')
def home():
    return "Welcome to the Fruit.ai API"

@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

@app.route('/api/faqs', methods=['POST'])
def create_faq():
    faq = request.get_json()
    faqs.append(faq)
    return jsonify(faq), 201

@app.route('/api/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    faq_data = request.get_json()
    for faq in faqs:
        if faq['id'] == id:
            faq.update(faq_data)
            return jsonify(faq)
    return jsonify({"error": "FAQ not found"}), 404

@app.route('/api/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    global faqs
    faqs = [faq for faq in faqs if faq['id'] != id]
    return '', 204

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
