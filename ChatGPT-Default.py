import openai

openai.api_key = "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"

def response (message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
        temperature=0,
        max_tokens=256
    )

    return print(response['choices'][0]['message']['content'])

message = input("물어봐: ")
response(message)