import pytest
from src.models.todo_list import ToDoList

@pytest.fixture
def todo_list():
    return ToDoList()

def test_add_task(todo_list):
    todo_list.add_task("Buy milk")
    assert any(task.description == "Buy milk" for task in todo_list.get_tasks())

def test_remove_task(todo_list):
    todo_list.add_task("Exercise")
    todo_list.remove_task("Exercise")
    assert all(task.description != "Exercise" for task in todo_list.get_tasks())

def test_remove_nonexistent_task(todo_list):
    with pytest.raises(ValueError):
        todo_list.remove_task("Non-existent")


def test_mark_task_completed(todo_list):
    todo_list.add_task("Read a book")
    todo_list.mark_task_completed("Read a book")
    assert todo_list.get_tasks()[0].completed == True

    with pytest.raises(ValueError):
        todo_list.mark_task_completed("Non-existent task")