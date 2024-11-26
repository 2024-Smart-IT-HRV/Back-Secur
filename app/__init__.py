from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # 데이터베이스 초기화
    db.init_app(app)

    # CORS 설정 추가
    CORS(app, resources={r"/auth/*": {"origins": "*"}})

    # 블루프린트 등록
    from auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
