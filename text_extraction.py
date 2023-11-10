answer = "'1','2','3','4','5'"
answerlist = [i for i, char in enumerate(answer) if char == "'"]  # answerlist는 모든 따옴표의 위치 인덱스를 담은 리스트
result = ''

while len(answerlist) >= 2:
    start_index = answerlist[0] + 1  # 첫 번째 따옴표 다음부터
    end_index = answerlist[1]  # 두 번째 따옴표 전까지
    result += answer[start_index:end_index]  # 첫 번째 따옴표와 두 번째 따옴표 사이에 있는 텍스트를 추가
    answerlist = answerlist[2:]  # 사용한 따옴표 인덱스 제거

print(result)