# import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI(api_key=api_key)


# response = openai.Image.create(
response = openai.images.generate(
    prompt = 'a dog and a cat which are close friends',
    n=1,
    size = '1024x1024'
)


# print(response.data[0].url)
print(response)