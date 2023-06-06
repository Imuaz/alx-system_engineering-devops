# 0x15. API

**INTRODUCTION**

The project covered a variety of topics related to programming and data formats. It began by discussing what Bash scripting should not be used for, providing guidance on its limitations. It then moved on to explain what an API is and provided an in-depth understanding of REST APIs and their characteristics. The project also covered the concept of microservices and their role in software architecture. Additionally, it provided explanations of the CSV and JSON formats, highlighting their uses and structures.

Furthermore, the project delved into Pythonic naming conventions for packages, modules, classes, variables, functions, and constants. It emphasized the significance of using consistent naming styles, such as CapWords or CamelCase, in Python code. Overall, this project offered a comprehensive exploration of programming concepts, data formats, and Python naming conventions, providing valuable insights for developers.

## Resources:books:
***Read or watch:***
- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [What is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices](https://smartbear.com/learn/api-design/microservices/)
- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- **Libraries imported in Python files must be organized in alphabetical order**
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- The code should use the `pycodestyle` (version `2.8.*`)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)')`
- [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) must be used to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- the code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks:page_with_curl:
**0. Gather data from an API**
- [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py): A Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.
  - It uses `urllib` or `requests` module
  - The script accepts an integer as a parameter, which is the employee ID
  - the script displays on the standard output the employee TODO list progress in this exact format:
    - First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS)`:
     1. `EMPLOYEE_NAME`: name of the employee
     2. `NUMBER_OF_DONE_TASKS`: number of completed tasks
     3. `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
    - Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)

**1. Export to CSV**
- [1-export_to_CSV.py](./1-export_to_CSV.py): `0-gather_data_from_an_API.py` extended to export data in the CSV format.
  - It records all tasks that are owned by this employee
  - format should be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS"`
  - `USER_ID.csv` is the file name

**2. Export to JSON**
- [2-export_to_JSON.py](./2-export_to_JSON.py): `0-gather_data_from_an_API.py` extended to export data in the JSON form.
  - It records all tasks that are owned by this employee
  - format should be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
  - `USER_ID.json` is the file name

**3. Dictionary of list of dictionaries**
- [3-dictionary_of_list_of_dictionaries.py](3-dictionary_of_list_of_dictionaries.py): `0-gather_data_from_an_API.py` extended to export data in the JSON form.
  - It records all tasks from all employees
  - format should be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
  - `todo_all_employees.json` is file name.

:+1:
