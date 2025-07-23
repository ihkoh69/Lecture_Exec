import os
from dotenv import load_dotenv
# import openai
from openai import OpenAI

load_dotenv()

# openai.api_key=os.getenv("OPENAI_APK_KEY")
api_key = os.getenv("OPENAI_API_KEY")

# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {
#             'role': 'system',
#             'content': '너는 아주 친절하고 똑똑한 비서야'
#         }
#     ]
# )

# print(response)

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 아주 친절하고 똑똑한 비서야"},
        {"role": "user", "content": "내게 3개 단락 분량으로 자기소개를 해줘. 소개는 전부 한국어로 진행해 줘"}
        
    ],
    temperature=2
)

print(response.choices[0].message.content)