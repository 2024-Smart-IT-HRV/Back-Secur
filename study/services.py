from datetime import datetime

def calculate_study_time(start_time, end_time):
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)
    duration = (end - start).total_seconds() / 60  # 분 단위로 변환
    return round(duration, 2)
