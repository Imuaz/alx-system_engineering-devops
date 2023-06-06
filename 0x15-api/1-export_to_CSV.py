#!/usr/bin/python3
"""Exports data in the CSV format"""

import requests
import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) <= 1 or not sys.argv[1].isdigit():
        sys.exit(0)

    BASE_API = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response_url = f"{BASE_API}users/{employee_id}"
    todo_response_url = f"{BASE_API}users/{employee_id}/todos"

    user_response = requests.get(user_response_url).json()
    todo_response = requests.get(todo_response_url).json()

    employee_name = user_response.get('name')
    username = user_response.get('username')

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        for todo in todo_response:
            task_status = str(todo.get("completed"))
            task_title = todo.get("title")
            writer.writerow([employee_id, username, task_status, task_title])

    print(f"Data exported to {filename}.")
