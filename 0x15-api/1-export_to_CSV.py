#!/usr/bin/python3
"""Exports data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = f"{userId}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        for task in todos.json():
            if task.get('userId') == int(userId):
                completed_status = str(task.get('completed'))
                task_title = task.get('title')
                writer.writerow([userId, name, completed_status, task_title])

    print(f"Data exported to {filename}.")
