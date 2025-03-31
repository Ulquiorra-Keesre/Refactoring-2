import os
import pytest
from src.storage.file_storage import FileStorage
from src.models.task import Task

@pytest.fixture
def storage():
    return FileStorage("test_tasks.json")

def test_save_and_load_tasks(storage):
    tasks = [Task("Task 1"), Task("Task 2", True)]
    storage.save_tasks(tasks)
    
    loaded_tasks = storage.load_tasks()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].description == "Task 1"
    assert loaded_tasks[1].completed == True


    os.remove("test_tasks.json") 




