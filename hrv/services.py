def calculate_focus_score(hrv_data):
    # HRV 데이터를 기반으로 집중력 점수 계산
    total_score = 0
    count = len(hrv_data)
    for data in hrv_data:
        total_score += data.hrv_data  # 심박 변이도 기반 점수 계산 로직
    return round(total_score / count, 2) if count > 0 else 0
