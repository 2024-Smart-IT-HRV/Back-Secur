from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth/signup", methods=["POST"])
def signup():
    """회원가입 API"""
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 필수 데이터 유효성 검사
    if not username or not email or not password:
        return jsonify({"error": "모든 필드를 입력해주세요."}), 400

    # 이메일 중복 확인
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "이미 사용 중인 이메일입니다."}), 400

    # 비밀번호 암호화 및 사용자 생성
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "회원가입이 완료되었습니다."}), 201


@auth_bp.route("/auth/login", methods=["POST"])
def login():
    """로그인 API"""
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # 사용자 조회
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "로그인 성공"}), 200

    return jsonify({"error": "아이디 혹은 비밀번호가 일치하지 않습니다."}), 401
