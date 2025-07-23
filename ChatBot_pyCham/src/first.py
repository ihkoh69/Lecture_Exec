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
#             'content': '너는 아주 친절하고 똑똑한 비서야.'
#         }
#     ]
# )

# print(response)

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 아주 친절하고 똑똑한 비서야."},
        {"role": "user", "content": "서울시 관악구의 오늘 날씨는 어때? 혹시 소나기가 올 확률이 있나?"}
    ]
)

print(response.choices[0].message.content)