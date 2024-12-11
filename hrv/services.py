#Back-Secur\hrv\services.py
import os
import csv

# CSV 파일 디렉토리 경로 설정
DATA_DIR = os.path.join(os.getcwd(), "data", "hrv")

# CSV 파일 읽기 함수
def read_csv_file(file_name):
    """
    주어진 파일 이름의 CSV 파일을 읽어서 데이터를 반환합니다.
    :param file_name: 읽을 CSV 파일의 이름 (예: '1.csv')
    :return: CSV 데이터의 리스트
    """
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일 {file_name}이(가) 존재하지 않습니다.")
    
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
    
    return data

# subject_id에 따라 CSV 파일 할당
def assign_csv_to_subject(subject_id):
    """
    주어진 subject_id에 따라 CSV 파일을 할당합니다.
    :param subject_id: 과목 ID
    :return: 할당된 CSV 파일 이름
    """
    csv_index = (subject_id % 7)  # 7로 나눈 나머지 값 계산
    if csv_index == 0:
        csv_index = 7  # 나머지가 0이면 7.csv로 설정
    assigned_file = f"{csv_index}.csv"
    return assigned_file

# subject_id에 해당하는 CSV 데이터 가져오기
def get_subject_data(subject_id):
    """
    특정 subject_id에 할당된 CSV 파일 데이터를 가져옵니다.
    :param subject_id: 과목 ID
    :return: subject_id에 할당된 CSV 데이터
    """
    assigned_file = assign_csv_to_subject(subject_id)
    data = read_csv_file(assigned_file)
    return data
