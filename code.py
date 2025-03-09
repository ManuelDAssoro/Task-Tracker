class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id #Each task has a unique id
        self.description = description #Description of the task
        self.status = status #Current status (todo, in-progress, done)
        self.createdAt = createdAt #Date and time of creation
        self.updatedAt = updatedAt #Date and time of last update

Tasks = []