from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # CORS 설정: 여러 경로를 한 번에 처리
    CORS(app, resources={
        r"/auth/*": {"origins": "*"},
        r"/study/*": {"origins": "*"}
    })

    # 데이터베이스 초기화
    db.init_app(app)

    # 블루프린트 등록
    from auth.routes import auth_bp
    from study.routes import study_bp

    app.register_blueprint(auth_bp)  # /auth 경로 등록
    app.register_blueprint(study_bp)  # /study 경로 등록

    # 데이터베이스 테이블 생성
    with app.app_context():
        db.create_all()

    return app
