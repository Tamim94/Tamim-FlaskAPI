import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for minimal baseline
USERS = {
    "1": {"id": "1", "username": "admin", "email": "admin@example.com"},
    "2": {"id": "2", "username": "developer", "email": "dev@example.com"}
}

@app.route('/health', methods=['GET'])
def health_check():
    """Basic health check endpoint."""
    return jsonify({"status": "up"}), 200

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    return jsonify(list(USERS.values())), 200

@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Returns details for a specific user."""
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    data = request.get_json() or {}
    if not data.get("username") or not data.get("email"):
        return jsonify({"error": "Missing username or email"}), 400

    new_id = str(len(USERS) + 1)
    new_user = {
        "id": new_id,
        "username": data["username"],
        "email": data["email"]
    }
    USERS[new_id] = new_user
    return jsonify(new_user), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
