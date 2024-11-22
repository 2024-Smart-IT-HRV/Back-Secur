from app import create_app

app = create_app()

@app.route("/")
def home():
    return "Welcome to the Flask API!"  # 기본 경로 응답

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/routes", methods=["GET"])
def list_routes():
    from flask import jsonify
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])