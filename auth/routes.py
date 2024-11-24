from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
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
        return jsonify({"token": token, "message": "로그인에 성공하였습니다."}), 200
    return jsonify({"error": "아이디 혹은 비밀번호가 일치하지 않습니다."}), 401

@auth_bp.route("/signup", methods=["POST", "OPTIONS"])
def signup():
    """사용자 회원가입 API"""
    if request.method == "OPTIONS":
        return jsonify({"message": "CORS preflight check passed"}), 200

    # POST 요청 처리
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 이메일 중복 확인
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "이미 사용 중인 이메일입니다."}), 400

    # 사용자 생성
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "회원가입이 완료되었습니다."}), 201
