#!/usr/bin/python3
"""
Export data in CSV format for a given employee ID
"""

import csv
import requests
import sys

if __name__ == '__main__':
    """
    REST API manipulations
    """
    if len(sys.argv) > 1 and isinstance(eval(sys.argv[1]), int):
        pass
    else:
        sys.exit(0)

    BASE_API = "https://jsonplaceholder.typicode.com/"
    emply_id = sys.argv[1]
    usr_response_url = BASE_API + "users/{}".format(emply_id)
    todo_response_url = BASE_API + "users/{}/todos".format(emply_id)

    usr_response = requests.get(usr_response_url).json()
    todo_response = requests.get(todo_response_url).json()

    emply_name = usr_response.get('name')

    taks_done = 0
    t_taks = 0
    t_records = []

    for todo in todo_response:
        t_taks += 1
        task_title = todo.get("title")
        comp_status = todo.get("completed")
        if comp_status:
            taks_done += 1
            t_records.append([emply_id, emply_name, comp_status, task_title])

    print("Employee {} is done with tasks({}\
    /{}):".format(emply_name, taks_done, t_taks))

    for task in t_records:
        print("\t {}".format(task[3]))

    csv_file_name = "{}.csv".format(emply_id)

    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        writer.writerows(t_records)

    print("Data exported to {}.".format(csv_file_name))
