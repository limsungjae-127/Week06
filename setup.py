import os

# 폴더 생성
directories = [
    "project_root",
    "project_root_pkg/gradebook/io",
    "project_root_pkg/tests"
]

for d in directories:
    os.makedirs(d, exist_ok=True)

# 파일 내용 정의
files = {
    ".gitignore": '''# Python cache files
__pycache__/
*.py[cod]
*$py.class

# Environments
.env
.venv
env/
venv/

# IDE settings
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
''',

    "README.md": '''# Python 활용 실습 과제 (GradeBook)

한경국립대학교 ICT로봇기계공학부 Python 활용 실습 과제입니다.

## 📁 프로젝트 구조

```text
GRADEBOOK/
├── .gitignore
├── README.md
├── gradebook.py
├── project_root/
│   ├── main.py
│   ├── models.py
│   └── utils.py
└── project_root_pkg/
    ├── students.csv
    ├── gradebook/
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── cli.py
    │   ├── models.py
    │   └── utils.py
    │   └── io/
    │       ├── __init__.py
    │       └── csvio.py
    └── tests/
        └── test_utils.py
```

## 🚀 실행 방법

### 1. 실습 1 (단일 파일 실행)
```bash
python gradebook.py
```

### 2. 실습 2 (모듈 분리 실행)
```bash
cd project_root
python main.py
cd ..
```

### 3. 실습 3 (패키지 CLI 실행)
```bash
cd project_root_pkg
python -m gradebook
cd ..
```

### 4. 실습 3 (단위 테스트 실행)
```bash
cd project_root_pkg
python -m unittest discover -s tests
cd ..
```
''',

    "gradebook.py": '''# ---------------------------
# 성적 계산 프로그램
# ---------------------------

def mean(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)

def main():
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])

    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    print("전체 반 평균 점수:", round(gb.class_average(), 2))

    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

if __name__ == "__main__":
    main()
''',

    "project_root/utils.py": '''# ---------------------------
# utils.py : 계산 관련 함수
# ---------------------------

def mean(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
''',

    "project_root/models.py": '''# ---------------------------
# models.py : 클래스 정의
# ---------------------------

from utils import mean, letter_grade

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)
''',

    "project_root/main.py": '''# ---------------------------
# main.py : 프로그램 시작
# ---------------------------

from models import Student, GradeBook

def main():
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])

    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    print("전체 반 평균 점수:", round(gb.class_average(), 2))

    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

if __name__ == "__main__":
    main()
''',

    "project_root_pkg/students.csv": '''Alice,90,85,92
Bob,70,75,68
Charlie,88,90,84
Diana,95,97,93
Ethan,60,65,58
''',

    "project_root_pkg/gradebook/__init__.py": '''# ---------------------------
# gradebook/__init__.py
# ---------------------------

"""
GradeBook 패키지

학생 성적 관리 프로그램
- utils: 평균, 학점 계산 함수
- models: Student, GradeBook 클래스
- io.csvio: CSV 파일 입출력
- cli: 명령행 실행 인터페이스
"""

from .models import Student, GradeBook
from .utils import mean, letter_grade

__all__ = ["Student", "GradeBook", "mean", "letter_grade"]
__version__ = "1.0.0"
''',

    "project_root_pkg/gradebook/__main__.py": '''# ---------------------------
# gradebook/__main__.py
# ---------------------------

"""패키지를 직접 실행할 수 있도록 진입점 제공"""

from .cli import run_cli

if __name__ == "__main__":
    run_cli()
''',

    "project_root_pkg/gradebook/cli.py": '''# ---------------------------
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

    print(f"\\n전체 반 평균 점수: {gb.class_average():.2f}\\n")
    for s in gb.students:
        print(f"{s.name}: 평균={s.average():.1f}, 학점={s.grade()}")
''',

    "project_root_pkg/gradebook/models.py": '''# ---------------------------
# gradebook/models.py
# ---------------------------

"""Student / GradeBook 클래스 정의"""

from .utils import mean, letter_grade

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

    def __repr__(self):
        return f"Student(name={self.name!r}, avg={self.average():.2f}, grade={self.grade()!r})"

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0
        return sum(s.average() for s in self.students) / len(self.students)

    def __repr__(self):
        return f"GradeBook({len(self.students)} students)"
''',

    "project_root_pkg/gradebook/utils.py": '''# ---------------------------
# gradebook/utils.py
# ---------------------------

"""성적 계산 관련 유틸리티 함수"""

def mean(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
''',

    "project_root_pkg/gradebook/io/__init__.py": '''# ---------------------------
# gradebook/io/__init__.py
# ---------------------------

"""입출력 관련 서브패키지"""

from .csvio import load_students_from_csv, save_students_to_csv

__all__ = ["load_students_from_csv", "save_students_to_csv"]
''',

    "project_root_pkg/gradebook/io/csvio.py": '''# ---------------------------
# gradebook/io/csvio.py
# ---------------------------

"""CSV 파일로부터 학생 정보를 읽고 쓰는 모듈"""

import csv
from ..models import Student

def load_students_from_csv(path):
    students = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            name = row[0]
            scores = [float(x) for x in row[1:]]
            students.append(Student(name, scores))
    return students

def save_students_to_csv(path, students):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for s in students:
            writer.writerow([s.name] + s.scores)
''',

    "project_root_pkg/tests/test_utils.py": '''# ---------------------------
# tests/test_utils.py
# ---------------------------

import unittest
from gradebook.utils import mean, letter_grade

class TestUtils(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([10, 20, 30]), 20)
        self.assertEqual(mean([]), 0.0)

    def test_letter_grade(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(65), "D")
        self.assertEqual(letter_grade(50), "F")

if __name__ == "__main__":
    unittest.main()
'''
}

# 파일 생성 및 저장
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# 불필요한 other_file.py 삭제
if os.path.exists("other_file.py"):
    os.remove("other_file.py")

print("✅ 모든 프로젝트 파일 생성이 완료되었습니다!")

