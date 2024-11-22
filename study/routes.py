from flask import Blueprint, request, jsonify
from app.models import Subject, StudyLog
from app import db

study_bp = Blueprint("study", __name__)

@study_bp.route("/subjects", methods=["POST"])
def add_subject():
    """과목 추가 API"""
    data = request.json
    user_id = data.get("user_id")
    subject_name = data.get("subject_name")

    # 요청 데이터 검증
    if not user_id or not subject_name:
        return jsonify({"error": "다시 입력 해주세요."}), 400

    # 과목 추가
    new_subject = Subject(user_id=user_id, subject_name=subject_name)
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({"message": "과목 추가 완료"}), 201

@study_bp.route("/logs", methods=["POST"])
def add_study_log():
    """공부 기록 저장 API"""
    data = request.json
    user_id = data.get("user_id")
    subject_id = data.get("subject_id")
    completed = data.get("completed")
    duration = data.get("duration")

    # 요청 데이터 검증
    if not user_id or not subject_id:
        return jsonify({"error": "Invalid log data"}), 400

    # 공부 기록 추가
    new_log = StudyLog(user_id=user_id, subject_id=subject_id, completed=completed, duration=duration)
    db.session.add(new_log)
    db.session.commit()
    return jsonify({"message": "공부 기록이 저장되었습니다."}), 201
