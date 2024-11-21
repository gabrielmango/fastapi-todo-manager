from fastapi import APIRouter, HTTPException

from app.todo.crud import get_all_todos, get_todo_by_id

todo_router = APIRouter()


@todo_router.get('/')
def list_todos():
    return get_all_todos()


@todo_router.get('/{todo_id}')
def retrieve_todo(todo_id: int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo
