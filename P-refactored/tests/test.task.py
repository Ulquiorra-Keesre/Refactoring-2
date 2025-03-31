import pytest
from src.models.task import Task

def test_task_creation():
    task = Task("Read a book")
    assert task.description == "Read a book"
    assert not task.completed

def test_task_completion():
    task = Task("Do homework")
    task.mark_completed()
    assert task.completed

def test_task_invalid_description():
    with pytest.raises(ValueError):
        Task("")
