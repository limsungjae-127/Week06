# ---------------------------
# gradebook/cli.py
# ---------------------------

"""명령행 실행 인터페이스 (CLI)"""

from .models import Student, GradeBook
from .io.csvio import load_students_from_csv

def run_cli():
    print("📘 GradeBook CLI 실행 중...")

    try:
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
