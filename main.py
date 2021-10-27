from fastapi import Body, FastAPI
from pydantic import BaseModel
from database import Base, engine
from routers import user


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(user.router)



@app.get("/")
def index():
    return  {"Hello": "world"}

@app.get("/say/{word}")
def say(word : str):
    return {"data":
    {
        "word": word
    }}