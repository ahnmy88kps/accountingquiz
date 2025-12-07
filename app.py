from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 총 10개의 O/X 회계 퀴즈 목록
QUIZ_QUESTIONS = [
    # 기존 5문제
    {
        "id": 1,
        "question": "선급공사비는 착공 전 발생한 비용이므로 공사원가에 해당한다.",
        "answer": "X",
    },
    {
        "id": 2,
        "question": "간이발급유형인 XX치킨집에서 특근식비를 집행하면 법인카드 정산시 B2 세금코드로 부가세 0원 처리한다.",
        "answer": "X",
    },
    {
        "id": 3,
        "question": "미청구공사, 미확정수익 계상시 미래 감액분 추정이 어려우니 보수적으로 실적정산분은 계상하지 않는다.",
        "answer": "X",
    },
    {
        "id": 4,
        "question": "개인카드 영수증도 회사 전표처리의 적격증빙이 될 수 있다.",
        "answer": "X",
    },
    {
        "id": 5,
        "question": "기부금영수증은 돈이 나갈 때 발행되는 현금주의 영수증이다.",
        "answer": "O",
    },
    # 새로 추가된 5문제
    {
        "id": 6,
        "question": "올해 착공한 A공사의 도급액은 10억원, 공정률은 50%, 매출세금계산서 발행 금액은 4억원일 경우, A공사의 올해 매출(수익)은 5억원이다.",
        "answer": "O",
    },
    {
        "id": 7,
        "question": "올해 착공한 B공사의 도급액은 10억원, 공정률은 10%, 매출세금계산서 발행 금액은 5억원일 경우, B공사의 올해 매출(수익)은 5억원이다.",
        "answer": "X",
    },
    {
        "id": 8,
        "question": "모든 경상 임차 사옥은 사용권자산으로 인식하여야 하며, 회계장부상 임차료를 인식하지 않는다.",
        "answer": "O", 
    },
    {
        "id": 9,
        "question": "당초 정당한 사유로 매출 세금계산서를 발급하였으나, 이후 정산분에 대해 감액이 발생한 경우 부(-)의 수정세금계산서를 발행한다.",
        "answer": "O", # (정답: 토지는 내용연수가 무한하므로 감가상각하지 않음)
    },
    {
        "id": 10,
        "question": "외국회사와 계약한 공사계약 수익은 수행 현장과 관련없이 모두 해외수익으로 분류한다.",
        "answer": "X",
    },
]

@app.route('/')
def index():
    """퀴즈 페이지를 렌더링합니다."""
    return render_template('quiz.html', questions=QUIZ_QUESTIONS)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    """사용자의 정답을 채점합니다."""
    results = []
    score = 0
    
    # 퀴즈 목록을 순회하며 정답과 비교
    for q in QUIZ_QUESTIONS:
        user_answer = request.form.get(f'q{q["id"]}') 
        is_correct = (user_answer == q["answer"])
        
        results.append({
            "id": q["id"],
            "question": q["question"],
            "user_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct,
        })
        
        if is_correct:
            score += 10

    return render_template('results.html', score=score, total=len(QUIZ_QUESTIONS), results=results)

if __name__ == '__main__':
    # Flask 앱을 실행합니다.

     app.run(debug=True, port=5001, use_reloader=False)


