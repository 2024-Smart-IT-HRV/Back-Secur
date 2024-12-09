from app import db

# 사용자 테이블
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
 # Remove `email` to match schema

    def __repr__(self):
        return f"<User {self.username}>"


# 과목 테이블
class Subject(db.Model):
    __tablename__ = "subjects"
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)  # Match `user_id` foreign key
    subject_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "user_id": self.user_id,
            "subject_name": self.subject_name,
            "created_at": self.created_at,
        }


# 학습 로그 테이블
class StudyLog(db.Model):
    __tablename__ = "study_logs"
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Match `log_id` in schema
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)  # Match `user_id` foreign key
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.subject_id"), nullable=False)  # Match `subject_id` foreign key
    completed = db.Column(db.Boolean, default=False)
    duration = db.Column(db.Integer, nullable=True)
    log_date = db.Column(db.DateTime, default=db.func.now())  # Add `log_date` to match schema

    def __repr__(self):
        return f"<StudyLog User:{self.user_id} Subject:{self.subject_id}>"
