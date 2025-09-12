from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index(limit, published:bool):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get('/blog/unpublished')
def unpublished():
      return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
        return {'data': f'blog id is {id}'}

@app.get('/blog/{id}/comments')

def comments(id):
      return {"data": {'4','2','3'}}

