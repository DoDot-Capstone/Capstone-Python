import openai

openai.api_key = "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"

def response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0,
        max_tokens=256
    )
    answer = response['choices'][0]['message']['content']
    answerlist = [i for i, char in enumerate(answer) if char == "'"]     #answerlist는 모든 따옴표의 위치 인덱스를 담은 리스트
    result = ''
    if len(answerlist) >= 2:
        start_index = answerlist[0] + 1  # 첫 번째 따옴표 다음부터
        end_index = answerlist[1]  # 두 번째 따옴표 전까지
        result += answer[start_index:end_index]  # 첫 번째 따옴표와 두 번째 따옴표 사이에 있는 텍스트를 추가
        answerlist = answerlist[2:]  # 사용한 따옴표 인덱스 제거
    return result #텍스트 전송

while True:
    message = input("물어봐: ")
    message = message + "라이브러리만 작은 따옴표로 표시 해주고 나머지는 아무런 표시 하지말고 따옴표 쓰지 말고 알려줘 코드랑 예제는 안 알려줘도 돼"
    print( response(message))