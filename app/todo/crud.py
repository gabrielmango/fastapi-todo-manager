from app.database import load_data, save_data


def get_all_todos():
    return load_data()
