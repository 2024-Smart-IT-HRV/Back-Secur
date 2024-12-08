from app import db

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    duration = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "subject_name": self.subject_name,
            "completed": self.completed,
            "duration": self.duration
        }
