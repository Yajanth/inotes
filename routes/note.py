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
            "notes":doc["note"]
        })

    return templates.TemplateResponse("index.html",{"request":request, "newdocs":newdocs})

@note.post('/')
def add_item(note : Note):
    inserted_note=conn.Notes.note.insertOne(dict(note))
    return noteEntity(inserted_note)