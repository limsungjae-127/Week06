# Python 활용 실습 과제 (GradeBook)

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
