#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1 or not sys.argv[1].isdigit():
        sys.exit(0)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{user_id}"
    todos_url = f"{base_url}todos"

    user_response = requests.get(user_url).json()
    username = user_response.get("username")

    todos_response = requests.get(todos_url, params={"userId": user_id}).json()
    tasks = []
    for todo in todos_response:
        task_title = todo.get("title")
        task_completed = todo.get("completed")
        tasks.append(
            {"task": task_title, "completed": task_completed, "username":
             username})

    data = {user_id: tasks}

    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {filename}.")
