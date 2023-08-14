from typing import Union

from fastapi import FastAPI, status, HTTPException
from dataclient import DataClient


app = FastAPI()

dataClient = DataClient()

@app.get("/")
def read_root():
    return {
        "info" : "This is simple todo app for managing your daily taksk",
        "tasks_list" : "/tasks",
        }


@app.get("/tasks/")
def read_tasks():
    return dataClient.getTasks()


@app.get("/tasks/{task_id}")
def read_task(task_id: int, q: Union[str, None] = None):
    tasks = dataClient.getTasks()
    result = None
    for task in tasks:
        if task.get("id") == task_id: #if task["id"] == task_id:
            result = task

    if (result == None):
        raise HTTPException(status_code=404, detail=status.HTTP_404_NOT_FOUND)
    else:
        return result


@app.post("/tasks/")
def create_task(task : dict):
    tasks = dataClient.getTasks()
    tasks.append(task)
    dataClient.updateTasks(tasks)
    return "Recieved"


@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_task: dict):
    tasks = dataClient.getTasks()
    for index, task in enumerate(tasks):
        if (task["id"] == task_id):
            tasks[index] = new_task
            dataClient.updateTasks(tasks)
            break
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
    
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = dataClient.getTasks()
    for task in tasks:
        if task.get("id") == task_id:
            tasks.remove(task)
            dataClient.updateTasks(tasks)
            break
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
    
    return task_id

