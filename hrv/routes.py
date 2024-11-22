from flask import Blueprint, request, jsonify
from app.models import HRVData
from app import db

hrv_bp = Blueprint("hrv", __name__)

@hrv_bp.route("/data", methods=["POST"])
def save_hrv():
    """HRV 데이터 저장 API"""
    data = request.json
    user_id = data.get("user_id")
    hrv_score = data.get("hrv_score")
    raw_data = data.get("raw_data")

    # 요청 데이터 검증
    if not user_id or not hrv_score:
        return jsonify({"error": "잘못된 경로 입니다."}), 400

    # 데이터 저장
    new_data = HRVData(user_id=user_id, hrv_score=hrv_score, raw_data=raw_data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "HRV data 측정 완료"}), 201

@hrv_bp.route("/data", methods=["GET"])
def get_hrv():
    """HRV 데이터 조회 API"""
    user_id = request.args.get("user_id")

    # 요청 데이터 검증
    if not user_id:
        return jsonify({"error": "잘못된 경로 입니다."}), 400

    # 데이터 검색
    data = HRVData.query.filter_by(user_id=user_id).all()
    if not data:
        return jsonify({"error": "데이터가 없습니다."}), 404

    # 결과 반환
    return jsonify([{
        "id": d.id,
        "user_id": d.user_id,
        "hrv_score": d.hrv_score,
        "timestamp": d.timestamp
    } for d in data]), 200
