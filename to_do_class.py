class Task:
    def __init__(self, name):
        self.name = name
        self.complete = False

    def task_complete(self):
        self.complete = True