# ---------------------------
# gradebook/cli.py
# ---------------------------

"""명령행 실행 인터페이스 (CLI)"""

import os
from .models import Student, GradeBook
from .io.csvio import load_students_from_csv

def run_cli():
    print("📘 GradeBook CLI 실행 중...")

    # 현재 파일 위치 기준으로 students.csv 경로 탐색
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "students.csv")

    try:
        if os.path.exists(csv_path):
            students = load_students_from_csv(csv_path)
        else:
            students = load_students_from_csv("students.csv")
    except FileNotFoundError:
        print("⚠️ students.csv 파일이 없습니다. 기본 데이터 사용.")
        students = [
            Student("Alice", [90, 85, 92]),
            Student("Bob", [70, 75, 68]),
        ]

    gb = GradeBook()
    for s in students:
        gb.add_student(s)

    print(f"\n전체 반 평균 점수: {gb.class_average():.2f}\n")
    for s in gb.students:
        print(f"{s.name}: 평균={s.average():.1f}, 학점={s.grade()}")
