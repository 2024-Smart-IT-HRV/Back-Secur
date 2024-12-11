from flask import Blueprint, request, jsonify
import os
import csv
import json
from threading import Lock

# Blueprint 생성
hrv_bp = Blueprint('hrv', __name__)

# CSV 파일 경로와 파일 목록
DATA_PATH = './data/hrv/'  # CSV 파일이 저장된 경로
CSV_FILES = [f"{i}.csv" for i in range(1, 8)]  # 1.csv부터 7.csv까지
read_pointers = {file: 0 for file in CSV_FILES}  # 각 파일의 읽기 위치 초기화
pointer_lock = Lock()  # Thread-Safe 관리를 위한 Lock

# Helper 함수: subject_id에 따라 CSV 파일 선택
def get_csv_file(subject_id):
    file_index = subject_id % 7
    if file_index == 0:
        file_index = 7
    return f"{file_index}.csv"

# Helper 함수: CSV에서 다음 행을 읽음
def read_next_row(file_name):
    global read_pointers

    file_path = os.path.join(DATA_PATH, file_name)

    # Thread-Safe 읽기
    with pointer_lock:
        current_pointer = read_pointers.get(file_name, 0)

    # CSV 파일 열기
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        rows = list(csv.DictReader(csv_file))
        if current_pointer >= len(rows):  # 모든 데이터를 읽었다면
            return None

        # 현재 포인터의 데이터를 반환
        row = rows[current_pointer]
        with pointer_lock:
            read_pointers[file_name] = current_pointer + 1

    return row

# 데이터 초기화 엔드포인트
@hrv_bp.route('/hrv/reset', methods=['POST'])
def reset_hrv():
    global read_pointers
    with pointer_lock:
        read_pointers = {file: 0 for file in CSV_FILES}  # 모든 포인터 초기화
    return jsonify({"message": "HRV 데이터가 초기화되었습니다."}), 200

# 현재 데이터 반환 엔드포인트
@hrv_bp.route('/hrv/get', methods=['GET'])
def get_hrv_data():
    subject_id = request.args.get('subject_id', type=int)
    if not subject_id:
        return jsonify({"error": "subject_id가 필요합니다."}), 400

    file_name = get_csv_file(subject_id)
    file_path = os.path.join(DATA_PATH, file_name)

    with pointer_lock:
        current_pointer = read_pointers.get(file_name, 0)

    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        rows = list(csv.DictReader(csv_file))
        if current_pointer >= len(rows):
            return jsonify({"message": "모든 데이터를 읽었습니다."}), 204
        row = rows[current_pointer]

    return jsonify(row), 200

# 다음 데이터 반환 엔드포인트
@hrv_bp.route('/hrv/next', methods=['GET'])
def get_next_hrv_data():
    subject_id = request.args.get('subject_id', type=int)
    if not subject_id:
        return jsonify({"error": "subject_id가 필요합니다."}), 400

    file_name = get_csv_file(subject_id)
    next_row = read_next_row(file_name)

    if not next_row:
        return jsonify({"message": "모든 데이터를 읽었습니다."}), 204

    return jsonify(next_row), 200

# 집중력 점수화 계산 엔드포인트
def normalize(value, min_val, max_val):
    if max_val - min_val == 0:  # Zero division guard
        return 0
    return (value - min_val) / (max_val - min_val) * 100  # 0~100 스케일

def calculate_focus_score(sdnn, rmssd, w_sdnn=0.5, w_rmssd=0.5):
    return w_sdnn * sdnn + w_rmssd * rmssd

@hrv_bp.route('/hrv/focus_score', methods=['GET'])
def get_focus_score():
    subject_id = request.args.get('subject_id', type=int)
    if not subject_id:
        return jsonify({"error": "subject_id가 필요합니다."}), 400

    file_name = get_csv_file(subject_id)
    next_row = read_next_row(file_name)

    if not next_row:
        return jsonify({"message": "모든 데이터를 읽었습니다."}), 204

    # 데이터 파싱
    try:
        raw_data = json.loads(next_row['hrv_rawdata'].replace("'", "\""))
        sdnn = float(raw_data["SDNN"])
        rmssd = float(raw_data["RMSSD"])
    except (KeyError, json.JSONDecodeError, ValueError) as e:
        return jsonify({"error": f"데이터 파싱 오류: {e}"}), 500

    # 정규화 및 점수 계산
    min_sdnn, max_sdnn = 20, 40
    min_rmssd, max_rmssd = 10, 30
    normalized_sdnn = normalize(sdnn, min_sdnn, max_sdnn)
    normalized_rmssd = normalize(rmssd, min_rmssd, max_rmssd)
    focus_score = calculate_focus_score(normalized_sdnn, normalized_rmssd)

    # 로그 추가
    print(f"Focus Score Calculated: {focus_score}")

    # 결과 반환
    result = {
        "timestamp": next_row["timestamp"],
        "focus_score": focus_score
    }
    return jsonify(result), 200
