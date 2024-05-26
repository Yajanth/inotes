from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="templates")

#Conncect the database
conn=MongoClient("mongodb://localhost:27017")


@app.get('/',response_class=HTMLResponse)
def index(request:Request):
    docs=conn.Notes.notes.find({})
    newdocs=[]
    for doc in docs:
        newdocs.append({
            "id":doc["_id"],
            "notes":doc["note"]
        })

    return templates.TemplateResponse("index.html",{"request":request, "newdocs":newdocs})

