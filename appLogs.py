from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='api_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger("api_application")

users = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Alice", "age": 25},
    {"id": 3, "name": "Bob", "age": 35}
]

def log_request_info():
    """Function to log information about the incoming request."""
    logger.info(f"Request received: {request.method} {request.url}")

@app.before_request
def before_request():
    """Function to be executed before each request."""
    log_request_info()

@app.route('/users', methods=['GET'])
def get_users():
    """Mock endpoint to get all users."""
    logger.info("Fetching all users")
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Mock endpoint to get a specific user."""
    logger.info(f"Fetching user with ID: {user_id}")
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        logger.error("User not found")
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Mock endpoint to create a new user."""
    data = request.get_json()
    logger.info(f"Creating user: {data}")
    new_user = {"id": len(users) + 1, "name": data["name"], "age": data["age"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
