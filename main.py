from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

tasks = []

class taskSchema(BaseModel):
    id:int
    taskName: str
    checked: bool

@app.get("/")
def root():
    return RedirectResponse("/docs")

@app.post("/task")
def createTask(task:taskSchema):
    tasks.append({
        "id":task.id,
        "taskName":task.taskName,
        "checked": task.checked
    })
    return "Successfully Created Task"

@app.put("/task/{id}")
def updateTask(id:int, task:taskSchema):
    for i, task in enumerate(tasks):
        if task.id == id:
            tasks[i] = {
            "id": task.id,
            "taskName": task.taskName,
            "checked": task.checked  
            }
    return "Successfully Updated Task"

@app.delete("/task/{id}")
def deleteTask(id:int, task:taskSchema):
    tasks = list(filter(lambda task: task.id != id, tasks))
    return "Successfully Deleted Task"

@app.get("/task")
def getTask():
    return tasks