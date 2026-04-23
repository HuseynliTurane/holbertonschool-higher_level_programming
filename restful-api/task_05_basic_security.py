from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Təhlükəsizlik açarları (Real layihədə bunları gizli saxlamalısınız)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# İstifadəçilərin siyahısı (Şərtə uyğun struktur)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Məntiqi ---
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

# --- JWT Error Handlers (Həmişə 401 qaytarmaq üçün) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Endpoint-lər ---

# 1. Basic Auth ilə qorunan route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# 2. Login (JWT token almaq üçün)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rol məlumatını tokenin içinə əlavə edirik (additional_claims)
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

# 3. JWT ilə qorunan route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# 4. Role-based (Yalnız Adminlər üçün) route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt() # Tokenin daxilindəki əlavə məlumatları (claims) alırıq
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run()
