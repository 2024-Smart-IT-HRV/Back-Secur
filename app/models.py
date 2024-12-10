from app import db

# 사용자 테이블
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


# 과목 테이블
class Subject(db.Model):
    __tablename__ = "subjects"
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "user_id": self.user_id,
            "subject_name": self.subject_name,
        }

    def __repr__(self):
        return f"<Subject {self.subject_name}>"


# 집중 점수 테이블
class FocusScore(db.Model):
    __tablename__ = "focus_scores"
    focus_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.subject_id"), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    focus_score = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {
            "focus_id": self.focus_id,
            "subject_id": self.subject_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "focus_score": self.focus_score,
        }

    def __repr__(self):
        return f"<FocusScore Subject ID: {self.subject_id}>"


# HRV 데이터 테이블
class HRVData(db.Model):
    __tablename__ = "hrv_data"
    hrv_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    focus_id = db.Column(db.Integer, db.ForeignKey("focus_scores.focus_id"), nullable=False)
    hrv_data = db.Column(db.Float, nullable=False)
    hrv_rawdata = db.Column(db.JSON, nullable=True)
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    def to_dict(self):
        return {
            "hrv_id": self.hrv_id,
            "user_id": self.user_id,
            "focus_id": self.focus_id,
            "hrv_data": self.hrv_data,
            "hrv_rawdata": self.hrv_rawdata,
            "timestamp": self.timestamp,
        }

    def __repr__(self):
        return f"<HRVData User ID: {self.user_id}, Focus ID: {self.focus_id}>"
