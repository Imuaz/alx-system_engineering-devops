#!/usr/bin/python3
"""
Script that exports to-do list information of all employees to JSON format.
"""
import json
import requests

if __name__ == "__main__":
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos_response.json()

    todo_all_employees = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]
        user_tasks = []

        for task in todos:
            if task["userId"] == user_id:
                task_title = task["title"]
                task_completed = task["completed"]
                task_dict = {
                    "username": username,
                    "task": task_title,
                    "completed": task_completed
                }
                user_tasks.append(task_dict)

        todo_all_employees[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(todo_all_employees, file)
