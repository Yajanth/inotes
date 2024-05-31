from pymongo import MongoClient

app=FastAPI()
#Conncect the database
conn=MongoClient("mongodb://localhost:27017")


