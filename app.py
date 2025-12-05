from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 총 10개의 O/X 회계 퀴즈 목록
QUIZ_QUESTIONS = [
    # 기존 5문제
    {
        "id": 1,
        "question": "재무상태표는 기업의 일정 기간 동안의 경영 성과를 나타낸다.",
        "answer": "X",
    },
    {
        "id": 2,
        "question": "감가상각은 자산의 가치 감소분을 비용으로 인식하는 회계 처리이다.",
        "answer": "O",
    },
    {
        "id": 3,
        "question": "매출액에서 매출원가를 뺀 금액을 당기순이익이라고 한다.",
        "answer": "X",
    },
    {
        "id": 4,
        "question": "부채는 미래의 경제적 효익이 유입될 것으로 기대되는 자원이다.",
        "answer": "X",
    },
    {
        "id": 5,
        "question": "자산은 '유동자산'과 '비유동자산'으로 분류된다.",
        "answer": "O",
    },
    # 새로 추가된 5문제
    {
        "id": 6,
        "question": "회계의 기본 등식은 '자산 = 부채 + 자본'이다.",
        "answer": "O",
    },
    {
        "id": 7,
        "question": "현금주의 회계는 현금이 실제로 들어오거나 나갈 때 수익과 비용을 인식한다.",
        "answer": "O",
    },
    {
        "id": 8,
        "question": "배당금 지급은 기업의 영업활동 현금흐름에 해당한다.",
        "answer": "X", # (정답: 재무활동 현금흐름)
    },
    {
        "id": 9,
        "question": "기업이 소유하고 있는 토지는 감가상각 대상 자산이다.",
        "answer": "X", # (정답: 토지는 내용연수가 무한하므로 감가상각하지 않음)
    },
    {
        "id": 10,
        "question": "대차평균의 원리는 차변 합계와 대변 합계가 항상 일치해야 한다는 것이다.",
        "answer": "O",
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
            score += 1

    return render_template('results.html', score=score, total=len(QUIZ_QUESTIONS), results=results)

if __name__ == '__main__':
    # Flask 앱을 실행합니다.
     app.run(debug=True, port=5001, use_reloader=False)