from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from auth.services import generate_token
from app.models import User
from app import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    """사용자 로그인 API"""
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # 사용자 검색
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        # 토큰 생성 및 반환
        token = generate_token(user.id)
        return jsonify({"token": "로그인에 성공하였습니다."}), 200
    return jsonify({"error": "아이디 혹은 비밀번호가 일치하지 않습니다."}), 401
