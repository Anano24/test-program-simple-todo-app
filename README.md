
# ___Test Program - Simple Todo App___



## __Definition__

This is a simple test program that simulates a Todo app with basic task management functionality. The program is implemented using FastAPI and utilizes a JSON file for data storage.


 ## __Overview__

 The test program demonstrates how to create, read, update, and delete tasks using a RESTful API. It includes a simple __DataClient__ class that interacts with a JSON file to store task data.


## __Features__
- Create a new task with an ID, title, and completion status.
- Retrieve a list of all tasks.
- Retrieve a specific task by its ID.
- Update task details by ID.
- Delete a task by ID.

## __Getting Started__
#### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn (or another ASGI server)

## __Usage__

+ Start the FastAPI application using Uvicorn:
    __uvicorn main:app --reload__
+ Open your web browser or API testing tool and access the provided URLs to interact with the API.



## __Endpoints__
- __GET /tasks/__
    - Retrieve a list of all tasks.
- __GET /tasks/{task_id}__
    - Retrieve details of a specific task by its ID.
- __POST /tasks/__
    - Create a new task. Requires a JSON payload with __id__, __title__, and __completed__ fields.
- __PUT /tasks/{task_id}__
    - Update the details of a task by its ID. Requires a JSON payload with the updated fields.
- __DELETE /tasks/{task_id}__
    - Delete a task by its ID.


## __Contributing__
Contributions to this test program are welcome! If you find any issues or have suggestions for improvements, please create a pull request or open an issue.



