from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date
import os
import pickle

app = FastAPI()


class TodoTask(BaseModel):
    task: str
    done: bool
    deadline: Optional[date]


if not os.path.exists('tasks.pkl'):
    with open('tasks.pkl', 'wb') as arq:
        pickle.dump([], arq)


@app.get('/tasks_list/{option}')
def tasks_list(option: str):
    with open('tasks.pkl', 'rb') as arq:
        tasks_list = pickle.load(arq)

    if option == "all":
        return tasks_list
    elif option == "done":
        tasks_list = list(filter(lambda x: x.done == True, tasks_list))
        return tasks_list
    elif option == "notdone":
        tasks_list = list(filter(lambda x: x.done == False, tasks_list))
        return tasks_list
    else:
        return {"error": "error when trying to read the tasks list"}


@app.post('/insert_task')
def insert(todo_task: TodoTask):
    with open('tasks.pkl', 'rb') as arq:
        tasks = pickle.load(arq)

    tasks.append(todo_task)

    with open('tasks.pkl', 'wb') as arq:
        pickle.dump(tasks, arq)

    return {"message": "task registered"}
