import os
import json
import pytest
from project import Load_ToDo, Add_goals, Add_reflexion

def test_Save_and_Load_ToDo(tmp_path, monkeypatch):

    os.makedirs(tmp_path / "data", exist_ok=True)
    tasks = [
        {"Name": "Test1", "Priority": 1, "Category": "Work", "Deadline": "07-21-2025", "Assigned day": "07-20-2025", "Finish day": None}
    ]
    test_file = tmp_path / "data" / "Tasks.json"
    with open(test_file, "w") as f:
        json.dump(tasks, f)
    monkeypatch.chdir(tmp_path)
    loaded = Load_ToDo()
    assert loaded == tasks

def test_Add_goals(tmp_path, monkeypatch):

    os.makedirs(tmp_path / "data", exist_ok=True)
    monkeypatch.chdir(tmp_path)
    TD_List = []
    task = Add_goals(
        TD_List,
        name="Read Book",
        priority=3,
        category="Personal",
        deadline="08-01-2025",
        test_mode=True
    )
    assert task in TD_List
    assert task["Name"] == "Read Book"
    assert task["Priority"] == 3
    assert os.path.exists("data/Tasks.json")


def test_Add_reflexion(tmp_path, monkeypatch):

    os.makedirs(tmp_path / "data", exist_ok=True)
    monkeypatch.chdir(tmp_path)
    result = Add_reflexion("Stay positive", "Nobody", test_mode=True)
    assert "Stay positive" in result
    assert os.path.exists("data/Reflexions.txt")
    with open("data/Reflexions.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "Stay positive" in content
