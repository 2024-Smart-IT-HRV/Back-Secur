from flask import Blueprint, request, jsonify
from app import db
from study.models import Subject

study_bp = Blueprint('study', __name__)

@study_bp.route('/subjects', methods=['GET'])
def get_subjects():
    # 사용자 ID를 쿼리 매개변수에서 가져옴
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "사용자 ID를 제공해야 합니다."}), 400

    # 데이터베이스에서 해당 사용자 ID에 해당하는 과목 조회
    subjects = Subject.query.filter_by(user_id=user_id).all()
    return jsonify([subject.to_dict() for subject in subjects]), 200


@study_bp.route('/subjects', methods=['POST'])
def add_subject():
    data = request.json
    print("Request JSON:", data)  # 요청 내용을 확인
    user_id = data.get('user_id')
    subject_name = data.get('subject_name')

    if not user_id or not subject_name:
        print("Missing Fields: user_id or subject_name is None")
        return jsonify({"error": "user_id와 subject_name을 모두 제공해야 합니다."}), 400

    new_subject = Subject(user_id=user_id, subject_name=subject_name)
    db.session.add(new_subject)
    db.session.commit()

    return jsonify({
        "message": "과목이 성공적으로 추가되었습니다.",
        "subject": new_subject.to_dict()
    }), 201


@study_bp.route('/subjects/<int:id>', methods=['DELETE'])
def delete_subject(id):
    # ID로 과목 검색
    subject = Subject.query.get(id)
    if not subject:
        return jsonify({"error": "삭제할 과목을 찾을 수 없습니다."}), 404

    # 과목 삭제
    db.session.delete(subject)
    db.session.commit()

    return jsonify({"message": "과목이 성공적으로 삭제되었습니다."}), 200
