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


chat_log = []

while True:

    user_input = input('무얼 원해? : ')
    if user_input == "stop":
        break

    chat_log.append({'role':'user', 'content': user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.5
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role':'assistant', 'content': bot_response})
    print(bot_response)