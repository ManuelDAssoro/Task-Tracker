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

path = './Tasks.json' #Define path as the Task's file path

def loadTasks(): #Saves the updated Tasks list to the file
    with open('Tasks.json','w') as outfile:
        json.dump([{ #Convert the Tasks list to a dictionary, and each attribute to string to be compatible with the JSON file
            'id': task.id,
            'description': task.description,
            'status': task.status,
            'createdAt': task.createdAt.isoformat(),
            'updatedAt': task.updatedAt.isoformat()
        } for task in Tasks], outfile)

if os.path.exists(path): #Check if path exist, if it doesn't create it
    print("Loading your Task list!")
else:
    print("No task list found! Creating a new one...")
    loadTasks()




def addTask(id, description, status, createdDate, updatedDate): #Add a task method
    task = Task(id, description, status, createdDate, updatedDate)
    Tasks.append(task)
    loadTasks()
    print("Task added")

def deleteTask(id): #Delete task method
    for task in Tasks:
        if task.id == id:
            Tasks.remove(task)
        print("Task deleted")
        loadTasks()

def updateTask(id):
    for task in Tasks:
        if task.id == id:
            print(task.description)
            task.description = input("Write the updated description ")
        print("Task updated")
        loadTasks()

def printTasks(): #Print all tasks and their attributes
    if not Tasks:
        print("There are no tasks") 
    for task in Tasks:
        print ("ID: ", task.id)
        print ("Description: ", task.description)
        print ("Status: ", task.status)
        print ("Created: ", task.createdAt)
        print ("Modified: ", task.updatedAt)
    


printTasks()
print("Add a new Task")
addTask(input("ID "),input("Description "),input("status "),date.today(), date.today()) #Test input
os.system("clear")
printTasks()
updateTask(input("Enter the ID to modify a Task")) #Test input
os.system("clear")
printTasks()
deleteTask(input("Enter the ID to delete a Task ")) #Test input
os.system("clear")
printTasks()