from fastapi import APIRouter, HTTPException

from app.todo.crud import (create_todo, get_all_todos, get_todo_by_id,
                           update_todo)
from app.todo.models import Todo

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


@todo_router.post('/')
def add_todo(todo: Todo):
    create_todo(todo.dict())
    return {'message': 'Todo created successfully'}


@todo_router.put('/{todo_id}')
def modify_todo(todo_id: int, todo: Todo):
    updated_todo = update_todo(todo_id, todo.dict())
    if not updated_todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return updated_todo
