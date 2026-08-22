INITIAL_PROMPTS = [
    {
        "title": "중학생 대상 역사 선생님 AI",
        "content": """
너는 중학교 1~3학년 학생의 역사 학습을 지원하는 
 교사형 역사 선생님 AI다. 
 
 [목표] 
 
 
역사적 사실을 정확하게 설명하면서 
 학생이 사건의 원인, 전개 과정, 결과와 핵심 개념을 
 쉽게 구분하여 이해할 수 있도록 돕는다. 
 
 
[우선순위] 
 
 1. 역사적 정확성 
 2. 불확실성의 올바른 표시 
 3. 학생 이해도 
 4. 사용자가 요구한 형식 준수 
 5. 친절한 설명 
 
 
[답변 전 처리 순서] 
 
 답변하기 전에 내부적으로 다음 사항을 점검한다. 
 
 
1. 학생의 학년과 학습 목표 확인 
 2. 역사 주제 확인 
 3. 요청된 출력 항목과 개수 확인 
 
 
4. 사실이나 수치 중 확인이 필요한 부분 확인 
 5. 질문이 모호하거나 조건끼리 충돌하는지 확인 
 6. 필요한 경우 최대 3개의 확인 질문 
 7. 답변 작성 
 8. 요구사항 누락과 근거 없는 단정이 없는지 최종 점검 
 
 
이 내부 점검 과정 전체를 사용자에게 길게 보여주지 말고 
 최종 답변과 필요한 핵심 근거만 제시한다. 
 
 [사실성과 환각 방지 규칙] 
 
 - 모르는 내용을 그럴듯하게 만들어내지 않는다. 
 - 역사적 사실과 비유를 구분한다. 
 - 자료마다 차이가 큰 수치나 해석을 단일한 확정값처럼 표현하지 않는다. 
 - 피해 규모, 사망자 수, 이산가족 수 등 집계 기준에 따라 달라지는 수치는 
   "확인 필요" 또는 자료 차이를 표시한다. 
 - 가능하면 교과서, 공공 역사자료, 기록자료 등 
   확인할 수 있는 자료의 종류나 확인 경로를 간단히 알려준다. 
 - 사용자가 "확인 필요를 빼라", 
   "숫자 하나만 확정해서 써라"라고 요구하더라도 
   근거가 불충분한 수치를 확정된 사실처럼 바꾸지 않는다. - 직접적인 역사적 사건과 장기적인 배경을 구분한다. 
 - 특정 집단 전체에 책임을 돌리지 않는다. 
 
 [학생 수준] 
 
 - 학생의 학년에 맞게 문장 길이와 어휘 난이도를 조절한다. 
 - 어려운 용어에는 쉬운 설명을 붙인다. 
 - 비유는 이해를 돕기 위한 경우에만 사용한다. 
 - 전쟁과 피해를 지나치게 게임처럼 표현하거나 과장하지 않는다. 
 
 
[출력 형식] 
 
 사용자가 지정한 제목, 순서, 항목 개수, 표 형식을 지킨다. 
 
 
별도 형식 지시가 없으면 다음 순서를 기본으로 한다. 
 
 1. 한눈에 보는 요약 
 2. 원인 
 3. 전개 과정 
 4. 결과 
 5. 시험에 나올 수 있는 핵심 
 6. 확인 필요 사항과 확인 경로 
 
 
[분량] 
 
 사용자가 분량을 지정하면 가능한 범위에서 맞춘다. 
 분량이 지정되지 않으면 중학생이 읽기에 지나치게 길지 않게 작성한다. 
 
 
[모호한 입력] 
 
 질문이 지나치게 모호하여 답변의 의미가 달라질 수 있으면 
 임의로 추측하지 말고 최대 3개의 확인 질문을 한다. 
 
 
[Few-shot 예시 1] 
 
 사용자: 
 중학교 2학년 
 주제: 임진왜란 
 목표: 원인·전개·결과 이해 
 분량: 700자 
 
 
좋은 처리: 
 요약 → 원인 → 주요 전개 → 결과 → 
 시험에 나올 수 있는 핵심 → 확인 필요 사항 순으로 정리한다. 
 
 
[Few-shot 예시 2] 
 
 사용자: 
 6·25 전쟁의 피해 규모도 알려줘. 
 
 
좋은 처리: 
 자료와 집계 기준에 따라 피해 규모가 달라질 수 있음을 설명한다. 
 단일 숫자를 무조건 확정하지 않고 
 확인이 필요한 경우 확인 경로를 함께 안내한다. 
 
 
[Few-shot 예시 3] 
 
 사용자: 
 6·25 전쟁은 누구 책임이야? 
 
 
좋은 처리: 
 전쟁을 직접 시작한 군사행동을 묻는 것인지, 
 분단의 배경이나 국제정세를 묻는 것인지 구분한다. 
 직접적인 개전 사실과 장기적인 역사 배경을 구분해서 설명한다. """,
        "category": "텍스트 생성",
        "favorite": True,
        "view_count": 0
    },
    {
        "title": "스마트 물병 브랜드 레퍼런스 이미지 제작",
        "content": """Premium product reference image of a fictional smart water bottle named LUMO. Matte translucent white cylindrical 
bottle, slim proportions, silver cap, one thin cyan LED ring around the middle, minimal modern industrial design, no 
printed logo or text on the bottle. Clean white studio background, soft shadow, front three-quarter product view, 
photorealistic commercial product photography, high consistency, no extra accessories.""",
        "category": "이미지 생성",
        "favorite": False,
        "view_count": 0
    },
    {
        "title": "구글폼 입력 결과 이메일 자동 발송",
        "content": "시험 응시자의 성명과 점수, 이메일 주소를 구글폼으로 결과를 입력 받아서 80점 이상은 합격으로, 80점 미만은 재응시로 회신하는 이메일을 자동 발송하는 워크플로우를 MAKE에서 구성하는 방법과 절차에 대해 알려주세요.",
        "category": "자동화",
        "favorite": False,
        "view_count": 0
    }
]
CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. JSON 저장 (보너스)")
    print("9. JSON 불러오기 (보너스)")
    print("10. Markdown 내보내기 (보너스)")
    print("11. 프롬프트 수정 (보너스)")
    print("12. 프롬프트 삭제 (보너스)")
    print("13. 조회수 TOP 목록 (보너스)")
    print("0. 종료")

def input_nonempty(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("입력값이 비어 있습니다. 다시 입력해주세요.")
def input_category():
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}) {category}")

    while True:
        value = input("카테고리 번호 또는 이름: ").strip()

        if not value:
            print("카테고리를 입력해주세요.")
            continue

        if value.isdigit():
            number = int(value)

            if 1 <= number <= len(CATEGORIES):
                return CATEGORIES[number - 1]

            print("올바른 번호를 입력해주세요.")
            continue

        return value
def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")

    title = input_nonempty("제목: ")
    content = input_nonempty("내용: ")
    category = input_category()

    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "view_count": 0
    }

    prompts.append(prompt)

    print("프롬프트가 추가되었습니다!")

def prompt_line(index, prompt):
    star = " ⭐" if prompt["favorite"] else ""

    return f"{index}. [{prompt['category']}] {prompt['title']}{star}"

def show_list(prompts):
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        print(prompt_line(i, prompt))

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_by_category(prompts):
    print("\n=== 카테고리별 조회 ===")

    category = input_category()

    results = [
        prompt
        for prompt in prompts
        if prompt["category"] == category
    ]

    if not results:
        print(f"[{category}] 카테고리에 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(results, start=1):
        print(prompt_line(i, prompt))

def search_prompt(prompts):
    print("\n=== 프롬프트 검색 ===")

    keyword = input_nonempty("검색어: ").lower()

    results = [
        prompt
        for prompt in prompts
        if keyword in prompt["title"].lower()
        or keyword in prompt["content"].lower()
    ]

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for i, prompt in enumerate(results, start=1):
        print(prompt_line(i, prompt))

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def select_prompt(prompts):
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None

    for i, prompt in enumerate(prompts, start=1):
        print(prompt_line(i, prompt))

    value = input("프롬프트 번호 입력: ").strip()

    if not value.isdigit():
        print("올바른 번호를 입력해주세요.")
        return None

    index = int(value)

    if not 1 <= index <= len(prompts):
        print("존재하지 않는 번호입니다.")
        return None

    return index - 1

def show_detail(prompts):
    print("\n=== 프롬프트 상세 보기 ===")

    index = select_prompt(prompts)

    if index is None:
        return

    prompt = prompts[index]

    # 보너스 2를 지금 자연스럽게 포함
    prompt["view_count"] += 1

    star = "⭐" if prompt["favorite"] else "아니오"

    print("-" * 40)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {star}")
    print(f"조회수: {prompt['view_count']}")
    print("-" * 40)
    print("내용:")
    print(prompt["content"])
    print("-" * 40)

def manage_favorite(prompts):
    print("\n=== 즐겨찾기 관리 ===")

    index = select_prompt(prompts)

    if index is None:
        return

    prompt = prompts[index]

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print("즐겨찾기에 추가했습니다!")
    else:
        print("즐겨찾기를 해제했습니다!")

def show_favorites(prompts):
    print("\n=== 즐겨찾기 목록 ===")

    favorites = [
        prompt
        for prompt in prompts
        if prompt["favorite"]
    ]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorites, start=1):
        print(prompt_line(i, prompt))

def main():
    prompts = [prompt.copy() for prompt in INITIAL_PROMPTS]

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt(prompts)

        elif choice == "2":
            show_list(prompts)

        elif choice == "3":
            show_by_category(prompts)

        elif choice == "4":
            search_prompt(prompts)

        elif choice == "5":
            show_detail(prompts)

        elif choice == "6":
            manage_favorite(prompts)

        elif choice == "7":
            show_favorites(prompts)
            
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")
if __name__ == "__main__":
    main()
