from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "AI service is running"}), 200

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello from your Agentic AI app!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
