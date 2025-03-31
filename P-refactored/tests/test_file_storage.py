import os
from src.storage.file_storage import FileStorage
from src.models.task import Task

def test_save_and_load_tasks():
    storage = FileStorage("test_tasks.json")
    tasks = [Task("Clean room"), Task("Go shopping", True)]
    storage.save_tasks(tasks)
    loaded_tasks = storage.load_tasks()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].description == "Clean room"
    assert loaded_tasks[1].completed

    os.remove("test_tasks.json") 
