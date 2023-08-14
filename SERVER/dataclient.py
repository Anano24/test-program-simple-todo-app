import json


class DataClient():
    def getTasks(self):
        with open("tasks.json", "r") as file:
            return json.loads(file.read())

    def updateTasks(self, tasks):
        with open("tasks.json", "w") as file:
            file.write(json.dumps(tasks))



