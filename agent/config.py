import os
from pathlib import Path

# 기본 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 제안서 관련 경로 설정
PROPOSAL_DIR = {
    'templates': os.path.join(BASE_DIR, 'data', 'templates'),  # 제안서 템플릿 폴더
    'source': os.path.join(BASE_DIR, 'data', 'source'),  # 제안서 원본 폴더
    'output': os.path.join(BASE_DIR, 'data', 'output'),     # 생성된 제안서 저장 폴더
}

# 제안서 템플릿 파일명 설정
PROPOSAL_TEMPLATES = {
    'basic': 'basic_proposal_template.txt',
    'detailed': 'detailed_proposal_template.txt',
}

# Vectorstore 관련 경로 설정
VECTORSTORE_DIR = {
    'db': os.path.join(BASE_DIR, 'data', 'vectorstore'), # Chroma DB 저장 폴더
}

# 필요한 디렉토리 생성
def create_directories():
    for directory in {**PROPOSAL_DIR, **VECTORSTORE_DIR}.values():
        os.makedirs(directory, exist_ok=True) 