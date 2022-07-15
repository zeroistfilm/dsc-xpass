from fastapi import FastAPI
import requests
app = FastAPI()

URL ='https://storage.googleapis.com/urbanbreakxpass2022/json/2000.json'

@app.get('/')
async def f():
    URL = 'https://storage.googleapis.com/urbanbreakxpass2022/json/2000.json'
    response = requests.get(URL)
    return response.json()





