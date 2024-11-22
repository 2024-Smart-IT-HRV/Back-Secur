from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# 데이터베이스와 마이그레이션 객체 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Flask와 데이터베이스 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트 등록
    from auth.routes import auth_bp
    from hrv.routes import hrv_bp
    from study.routes import study_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(hrv_bp, url_prefix="/hrv")
    app.register_blueprint(study_bp, url_prefix="/study")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트 등록
    from auth.routes import auth_bp
    from hrv.routes import hrv_bp
    from study.routes import study_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(hrv_bp, url_prefix="/hrv")
    app.register_blueprint(study_bp, url_prefix="/study")

    # 기본 라우트('/')
    @app.route('/')
    def index():
        return {"message": "Welcome to the Flask API!"}, 200

    return app
