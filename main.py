from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}


@app.get('/blog/unpublished')
def unpublished():
      return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
        return {'data': f'blog id is {id}'}

@app.get('/blog/{id}/comments')

def comments(id):
      return {"data": {'4','2','3'}}

