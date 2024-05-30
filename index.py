from fastapi import FastAPI
from route.notes import note

app=FastAPI()
app.include_router(note)
