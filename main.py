from fastapi import FastAPI

app = FastAPI()

titles = []
descriptions = []
prioritys = ["High", "Medium", "Low"]
deadlines = []
statuses = ["Untouched", "Just Started", "Half-Done", "Mostly Done", "Completed"]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/task")
def createTask(title: str, description: str, priority: str, deadline: str, status: str):
    titles.append(title)
    descriptions.append(description)
    deadlines.append(deadline)
    return {"message": "Task Created"}

@app.get("/task/priority/{priority_id}")
def getPriority(priority_id: int):
    priority = prioritys[priority_id]
    return priority

@app.get("/task/status/{status_id}")
def getStatus(status_id: int):
    status = statuses[status_id]
    return status

#@app.get("/task")
#def getTask():
