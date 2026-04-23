from flask import Flask, jsonify, request

app = Flask(__name__)

# Yaddaşda istifadəçiləri saxlamaq üçün lüğət
users = {}

@app.route("/")
def home():
    """Ana səhifə üçün endpoint."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Sistemdəki bütün istifadəçi adlarını (username) siyahı kimi qaytarır."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """API-nin vəziyyətini yoxlamaq üçün endpoint."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Dinamik route: Verilən istifadəçi adına görə məlumatları qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """POST sorğusu vasitəsilə yeni istifadəçi əlavə edir."""
    # JSON-un düzgünlüyünü yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Username mövcudluğunu yoxlayırıq
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Username-in təkrar olub-olmadığını yoxlayırıq
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yeni istifadəçini lüğətə əlavə edirik
    users[username] = data

    # Uğurlu cavab qaytarırıq (201 Created statusu ilə)
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
