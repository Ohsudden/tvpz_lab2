from flask import Flask, request, jsonify

app = Flask(__name__)

# Емуляція бази даних
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    users[data['email']] = data['password']
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True)
