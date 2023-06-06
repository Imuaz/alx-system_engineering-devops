#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/\
                                 {user_id}")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()
        todos = todos_response.json()

        total_tasks = 0

        completed_tasks = []

        for task in todos:
            if task.get('userId') == int(user_id):
                total_tasks += 1
                if task.get('completed'):
                    completed_tasks.append(task)
                    print(f"Employee {user['name']} is done with tasks\
                          ({len(completed_tasks)}/{total_tasks}):")
                    for task in completed_tasks:
                        print(f"\t{task['title']}")
    else:
        print("Failed to retrieve data from the API.")
