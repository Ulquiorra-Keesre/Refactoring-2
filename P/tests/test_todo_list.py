import pytest
from src.models.todo_list import ToDoList
from src.models.task import Task

@pytest.fixture
def todo_list():
    return ToDoList()

def test_add_task(todo_list):
    todo_list.add_task("Buy milk")
    assert len(todo_list.get_tasks()) == 1
    assert todo_list.get_tasks()[0].description == "Buy milk"

def test_remove_task(todo_list):
    todo_list.add_task("Do homework")
    todo_list.remove_task("Do homework")
    assert len(todo_list.get_tasks()) == 0

    with pytest.raises(ValueError):
        todo_list.remove_task("Non-existent task")

def test_mark_task_completed(todo_list):
    todo_list.add_task("Read a book")
    todo_list.mark_task_completed("Read a book")
    assert todo_list.get_tasks()[0].completed == True

    with pytest.raises(ValueError):
        todo_list.mark_task_completed("Non-existent task")




