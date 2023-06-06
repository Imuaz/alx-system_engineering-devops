#!/usr/bin/python3
"""
Python script that retrieves to-do list information for a given employee ID
using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"

        user_response = requests.get(f"{base_url}users/{employee_id}")
        todos_response = requests.get(f"{base_url}todos?userId={employee_id}")

        if user_response.status_code == 200 and todos_response.status_code ==\
                200:
            user = user_response.json()
            todos = todos_response.json()

            completed_tasks = [task for task in todos if task["completed"]]
            count = len(completed_tasks)
            all_tasks = len(todos)

            print(f"Employee {user['name']} is done with tasks({count}\
                  /{all_tasks}):")
            for task in completed_tasks:
                print(f"\t{task['title']}")
            else:
                print("Failed to retrieve data from the API.")
