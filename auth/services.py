#auth/services.py
import jwt
import datetime
from app.config import Config

def generate_token(user_id):
    """JWT 토큰 생성"""
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
