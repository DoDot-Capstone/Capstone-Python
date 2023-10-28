import os
import openai

openai.organization = "org-1XXm4ES0ovolFy2Ck73BlgG3"
openai.api_key = "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"
openai.Model.list()

message = input("물어봐 : ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": str(message)},
    ],
    temperature=0,
    max_tokens=256
)

print(response)

# print(chr(response.choices[0].message.content))