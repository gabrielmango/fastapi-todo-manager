from fastapi import APIRouter

from app.todo.crud import get_all_todos

todo_router = APIRouter()


@todo_router.get('/')
def list_todos():
    return get_all_todos()
