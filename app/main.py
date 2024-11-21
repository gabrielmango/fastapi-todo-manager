from fastapi import FastAPI

from app.todo.routes import todo_router

app = FastAPI()

app.include_router(todo_router, prefix='/api/todos', tags=['Todos'])
