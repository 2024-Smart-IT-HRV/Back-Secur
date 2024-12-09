from flask import Blueprint, request, jsonify
from app import db
from app.models import Subject
from app.utils import token_required

study_bp = Blueprint('study_bp', __name__)

@study_bp.route('/subjects', methods=['GET'])
@token_required
def get_subjects():
    user_id = request.user_id
    subjects = Subject.query.filter_by(user_id=user_id).all()
    return jsonify([subject.to_dict() for subject in subjects]), 200

@study_bp.route('/subjects', methods=['POST'])
@token_required
def add_subject():
    user_id = request.user_id
    data = request.json
    subject_name = data.get('subject_name')

    if not subject_name:
        return jsonify({"error": "subject_name을 제공해야 합니다."}), 400

    new_subject = Subject(user_id=user_id, subject_name=subject_name)
    db.session.add(new_subject)
    db.session.commit()

    return jsonify({"message": "과목이 성공적으로 추가되었습니다.", "subject": new_subject.to_dict()}), 201

@study_bp.route('/subjects/<int:id>', methods=['DELETE'])
@token_required
def delete_subject(id):
    user_id = request.user_id
    subject = Subject.query.filter_by(subject_id=id, user_id=user_id).first()

    if not subject:
        return jsonify({"error": "삭제할 과목을 찾을 수 없습니다."}), 404

    db.session.delete(subject)
    db.session.commit()
    return jsonify({"message": "과목이 성공적으로 삭제되었습니다."}), 200

@study_bp.route('/subjects/<int:id>', methods=['OPTIONS'])
def options_subject(id):
    return '', 200
