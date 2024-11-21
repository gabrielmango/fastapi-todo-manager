from app.database import load_data, save_data


def get_all_todos():
    return load_data()


def get_todo_by_id(todo_id: int):
    todos = load_data()
    return next((todo for todo in todos if todo['id'] == todo_id), None)


def create_todo(todo: dict):
    todos = load_data()
    todos.append(todo)
    save_data(todos)


def update_todo(todo_id: int, updated_todo: dict):
    todos = load_data()
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos[index] = updated_todo
            save_data(todos)
            return updated_todo
    return None
