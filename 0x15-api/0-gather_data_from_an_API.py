#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(
        base_url + f"users/{employee_id}"
    ).json()
    todos_response = requests.get(
        base_url + f"todos?userId={employee_id}"
    ).json()

    employee_name = user_response.get("name")

    completed_tasks = [
        todo.get("title") for todo in todos_response if todo.get("completed")
    ]
    num_tasks_done = len(completed_tasks)
    total_num_tasks = len(todos_response)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({num_tasks_done}/{total_num_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")
