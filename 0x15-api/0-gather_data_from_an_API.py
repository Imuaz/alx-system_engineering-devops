#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_response = requests.get(base_url + f"users/{employee_id}")
    todos_response =\
        requests.get(base_url + "todos", params={"userId": employee_id})

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()
        todos = todos_response.json()

        completed = [t["title"] for t in todos if t["completed"]]
        print(f"Employee {user['name']} is done with tasks ({len(completed)}\
              /{len(todos)}):")
        for task in completed:
            print(f"\t{task}")
    else:
        print("Failed to retrieve data from the API.")
