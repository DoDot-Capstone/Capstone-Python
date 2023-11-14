import re
import openai

openai.api_key = "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"

def response (message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"프로그래밍할 때 필요한 라이브러리를 추천해줍니다."},
            {"role":"user", "content":message},
            {"role":"user", "content":"프로그래밍할 때 필요한 라이브러리만 추천해줘야해, 무조건 라이브러리 이름에 해당하는 부분은 양 옆에 !!!를 넣어서 표시해줘."}
        ],
        temperature=0,
        max_tokens=256
    )

    return response['choices'][0]['message']['content']

message = input("물어봐: ")
result = response(message)

result = str(result)

print(result)

p = re.compile('!!!(.+?)!!!')

list = p.findall(str(result))

print("\n")
print("for list")
for msg in list:
    print(msg)
