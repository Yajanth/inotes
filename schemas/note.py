def noteEntity(item)->dict:
    return { 
        "id":str(item["_id"]),
        "title":str(item["title"]),
        "Desc": item["Desc"],
        "Important":item["Important"]} #converting mongodb object to pythonic dictionary


def notesEntity(item)->list:
    return [noteEntity(item) for item in items]
