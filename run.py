from flask_cors import CORS
from app import create_app

app = create_app()

# CORS 설정: 모든 출처와 모든 HTTP 메서드 허용
CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)  # Debug 모드 활성화
