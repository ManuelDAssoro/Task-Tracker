import time
import os
import json
from datetime import date

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id #Each task has a unique id
        self.description = description #Description of the task
        self.status = status #Current status (todo, in-progress, done)
        self.createdAt = createdAt #Date and time of creation
        self.updatedAt = updatedAt #Date and time of last update

Tasks = []

def loadTasks(): #Load the Tasks list from the file
    global Tasks
    with open("/home/manuel/roadmap/Tasks.json", "r") as f:
        task_dicts = json.load(f)
        Tasks = [Task(task['id'], task['description'], task['status'], date.fromisoformat(task['createdAt']), date.fromisoformat(task['updatedAt'])) for task in task_dicts]

def saveTasks(): #Saves the updated Tasks list to the file
    with open("Tasks.json","w") as f:
        json.dump([{ #Convert the Tasks list to a dictionary, and each attribute to string to be compatible with the JSON file
            'id': task.id,
            'description': task.description,
            'status': task.status,
            'createdAt': task.createdAt.isoformat(),
            'updatedAt': task.updatedAt.isoformat()
        } for task in Tasks], f)

def addTask(): #Add a task method 
    print("Add a new Task")
    flag = 0
    while (flag == 0):
        id = input("ID: ")
        if any(task.id == id for task in Tasks):
            print("ID already exists")
        else:
            flag = 1;
    description = input("Description: ")
    status = input("Status: ")
    createdDate = date.today()
    updatedDate = date.today()
    task = Task(id, description, status, createdDate, updatedDate)    
    Tasks.append(task)
    saveTasks()
    print("Task added")

def deleteTask(id): #Delete task method
    for task in Tasks:
        if task.id == id:
            Tasks.remove(task)
        print("Task deleted")
        saveTasks()

def updateTask(id):
    for task in Tasks:
        if task.id == id:
            print(task.description)
            task.description = input("Write the updated description ")
        print("Task updated")
        saveTasks()

def printTasks(): #Print all tasks and their attributes
    if not Tasks:
        print("There are no tasks") 
    for task in Tasks:
        print ("ID: ", task.id)
        print ("Description: ", task.description)
        print ("Status: ", task.status)
        print ("Created: ", task.createdAt)
        print ("Modified: ", task.updatedAt)
    
def printDoneTasks(): #Print all tasks that are done
    for task in Tasks:
        if task.status == "done":
            print ("ID: ", task.id)
            print ("Description: ", task.description)
            print ("Status: ", task.status)
            print ("Created: ", task.createdAt)
            print ("Modified: ", task.updatedAt)

def printToDoTasks(): #Print all tasks that are not done
    for task in Tasks:
        if task.status == "todo":
            print ("ID: ", task.id)
            print ("Description: ", task.description)
            print ("Status: ", task.status)
            print ("Created: ", task.createdAt)
            print ("Modified: ", task.updatedAt)   

def printInProgressTasks(): #Print all tasks that are in progress
    for task in Tasks:
        if task.status == "in-progress":
            print ("ID: ", task.id)
            print ("Description: ", task.description)
            print ("Status: ", task.status)
            print ("Created: ", task.createdAt)
            print ("Modified: ", task.updatedAt)

def markInProgress(id): #Mark a task as in progress
    for task in Tasks:
        if task.id == id:
            task.status = "in-progress"
            task.updatedAt = date.today()
        print("Task marked as in progress")
        saveTasks()

def markDone(id): #Mark a task as done
    for task in Tasks:
        if task.id == id:
            task.status = "done"
            task.updatedAt = date.today()
        print("Task marked as done")
        saveTasks()

