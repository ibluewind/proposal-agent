from agent.config import PROPOSAL_DIR, PROPOSAL_TEMPLATES, create_directories
import os

def proposal_agent(prompt: str) -> str:
    # 필요한 디렉토리 생성
    create_directories()
    
    # 기본 템플릿 파일 경로
    template_path = os.path.join(
        PROPOSAL_DIR['templates'], 
        PROPOSAL_TEMPLATES['basic']
    )
    
    # 결과물 저장 경로
    output_path = os.path.join(
        PROPOSAL_DIR['output'], 
        f"proposal_{prompt[:30]}.txt"  # 파일명에 주제 일부 사용
    )
    
    # TODO: 템플릿을 기반으로 제안서 생성 로직 구현
    return prompt

if __name__ == "__main__":
    user_prompt = input("제안서 주제를 입력해주세요: ")
    result = proposal_agent(user_prompt)
    print(result)
