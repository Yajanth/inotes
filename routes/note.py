from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.note import Note
from schemas.note import noteEntity , notesEntity
from config.db import conn 

note=APIRouter()
templates=Jinja2Templates(directory="templates")


@note.get('/',response_class=HTMLResponse)
def index(request:Request):
    docs=conn.Notes.notes.find({})
    newdocs=[]
    for doc in docs:
        newdocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":["important"]
        })

    return templates.TemplateResponse("index.html",{"request":request, "newdocs":newdocs})


@note.post('/')
async def create_item(request : Request):
    form=await request.form()
    formDict=dict(form)
    formDict['important']=True if formDict.get("important")=="on" else False
    note=conn.Notes.notes.insert_one(formDict)
    return {"Success": True}




