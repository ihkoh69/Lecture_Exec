import os
from dotenv import load_dotenv
# import openai
from openai import OpenAI
from fastapi import FastAPI, Form, Request
# pip install python-multipart
# pip install fastapi\[all\]. 
# pip install fastapi[all]
# pip install uvicorn
# pip install aiofiles jinja2
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")




load_dotenv()

# openai.api_key=os.getenv("OPENAI_API_KEY")
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

chat_responses = []

chat_log = [{'role': 'system', 
             'content': 'You are a python tutor AI, completely dedicated to teach users how to learn \
              python from scratch. Please provide clear instructions on python concepts, \
              best practices and syntax. Help create a path of learning for users to be able \
              to create real life, production ready python applications.'
            }]

# chat_log = [{'role': 'system', 
#              'content': ('You are a python tutor AI, completely dedicated to teach users how to learn '
#               'python from scratch. Please provide clear instructions on python concepts, '
#               'best practices and syntax. Help create a path of learning for users to be able '
#               'to create real life, production ready python applications.')
#             }]



@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})




@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
# async def chat(user_input: Annotated[str, Form()]):
    
    chat_log.append({'role': 'system', 'content': user_input})
    chat_responses.append(user_input)


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.5
    )
    
    bot_response = response.choices[0].message.content
    chat_log.append({'role':'assistant', 'content': bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})
    # return bot_response

@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})


@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):
    response = client.images.generate(
        prompt=user_input,
        n=1,
        size='512x512'
    )
    
    image_url = response.data[0].url
    print(image_url)
    
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})