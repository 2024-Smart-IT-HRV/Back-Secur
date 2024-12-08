from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class HRVData(db.Model):
    __tablename__ = "hrv_data"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    hrv_score = db.Column(db.Float, nullable=False)
    raw_data = db.Column(db.JSON, nullable=True)
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=False)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    duration = db.Column(db.Integer, default=0)  # 초 단위 학습 시간

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "subject_name": self.subject_name,
            "completed": self.completed,
            "duration": self.duration
        }

class StudyLog(db.Model):
    __tablename__ = "study_logs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    duration = db.Column(db.Integer, nullable=True)
