class Config:
    SECRET_KEY = "your-secret-key"  # 비밀 키 설정
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"  # 데이터베이스 URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
