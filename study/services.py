from datetime import datetime
from app.models import StudyLog  # 수정된 경로


def calculate_study_time(start_time, end_time):
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)
    duration = (end - start).total_seconds() / 60  # 분 단위로 변환
    return round(duration, 2)

def validate_subject_data(data):
    if not data.get('user_id') or not data.get('subject_name'):
        return "user_id와 subject_name이 필요합니다."
    return None
