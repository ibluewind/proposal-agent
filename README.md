# Proposal Agent

## 목차

1. 제안서 생성 에이전트
2. 벡터 스토어 생성
3. 기능 분류


### 1. 제안서 생성 에이전트
- 사용자로 부터 제안서 주제를 입력받아 제안서를 생성하는 에이전트
- 제안서 벡터 스토어로부터 주제에 대한 정보 검색
- 검색 결과와 프롬프트를 통해 Markdown 형식의 제안서 생성
- Markdown 형식의 제안서를 PPT로 변환
- 생성된 PPT를 파일로 저장

### 2. 벡터 스토어 생성
#### 2-1. PPT 문서 변환
- PPT를 Markdown 형식으로 변환한다.
  - PPT 페이지 단위로 Document화
  - '#' 표지
  - '##' Sub-title
  - 'Content' 본문
#### 2-2. 벡터 스토어 생성
- 특정 폴더에 있는 PPT 파일(** 우선은 PPT 파일만 사용)을 벡터 스토어로 생성
- 벡터 스토어는 Chroma 라이브러리를 사용하여 생성

### 3. 기능 분류
- 벡터 스토어 생성
- 벡터 스토어 검색
- 제안서 생성
- 제안서 파일 저장