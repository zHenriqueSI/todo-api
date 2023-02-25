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
