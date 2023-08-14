import requests



class TaskClient:
    BASE_URL = "http://127.0.0.1:8000/tasks/"

    def create_task(self, **task):
        return requests.post(f"{TaskClient.BASE_URL}", json=task).json()
        

    def get_task(self, task_id):
        return requests.get(f"{TaskClient.BASE_URL}{task_id}").json()

    def get_all_tasks(self):
        return requests.get(f"{TaskClient.BASE_URL}").json()
        
    
    def update_task(self, task_id, **task):
        return requests.put(f"{TaskClient.BASE_URL}{task_id}", json=task).json()

    def delete_task(self, task_id):
        return requests.delete(f"{TaskClient.BASE_URL}{task_id}").json()

        
    @classmethod
    def choice(cls):
        try:
            n = int(input("Enter your choice: "))
            if n not in [1, 2, 3, 4, 5, 0]:
                raise ValueError()
            return n
        except ValueError:
            print("Please enter a valid choice (1, 2, 3, 4, 5, or 0)")
            return cls.choice()


# this is the user input program
def main():
    
    print(
        "Command - Task Management",
        "1. Create a task",
        "2. Get a task by ID",
        "3. Get all tasks",
        "4. Update a task",
        "5. Delete a task",
        "0. Exit",
        sep = "\n"
    )

    client_choice = TaskClient.choice()
    client = TaskClient()

    if client_choice == 1:
        id = int(input("Enter id: "))
        title = input("Enter the task title: ")
        completed = input("Is the task completed? (True/False): ")
        task = {"id" : id, "title": title, "completed": completed}
        print(client.create_task(**task))
    elif client_choice == 2:
        n = int(input("Enter id: "))
        response = client.get_task(n)
        print(response)
    elif client_choice == 3:   
        tasks = client.get_all_tasks()
        print(tasks)
    elif client_choice == 4:
        id = int(input("Enter id: "))
        title = input("Enter the task title: ")
        completed = input("Is the task completed? (True/False): ")
        task = {"id" : id,  "title": title, "completed": completed}
        print(client.update_task(id, **task))
    elif client_choice == 5:
        task_id = int(input("Enter the task ID: "))
        response = client.delete_task(task_id)
        print(response)




if __name__ =="__main__":
    main()

