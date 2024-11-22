from marshmallow import Schema, fields, ValidationError

# 로그인 데이터 스키마
class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

# 과목 추가 데이터 스키마
class SubjectSchema(Schema):
    user_id = fields.Integer(required=True)
    subject_name = fields.String(required=True)

# 공부 기록 데이터 스키마
class StudyLogSchema(Schema):
    user_id = fields.Integer(required=True)
    subject_id = fields.Integer(required=True)
    completed = fields.Boolean(required=True)
    duration = fields.Integer(required=True)

def validate_input(schema, data):
    """입력 데이터 검증 함수"""
    try:
        schema.load(data)
    except ValidationError as err:
        return err.messages
    return None
