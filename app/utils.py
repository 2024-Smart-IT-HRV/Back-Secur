from functools import wraps
from flask import request, jsonify
import jwt
from app.config import Config

def token_required(f):
    """JWT 토큰 검증 데코레이터"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "인증 토큰이 필요합니다."}), 401

        try:
            token = token.split(" ")[1]  # "Bearer <token>"에서 토큰 추출
            decoded = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            request.user_id = decoded.get('user_id')
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "토큰이 만료되었습니다."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "유효하지 않은 토큰입니다."}), 401

        return f(*args, **kwargs)
    return decorated
