from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return  {"Hello": "world"}

@app.get("/say/{word}")
def say(word : str):
    return {"data":
    {
        "word": word
    }}