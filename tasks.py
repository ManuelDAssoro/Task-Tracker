import time
import os
from datetime import date
class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id #Each task has a unique id
        self.description = description #Description of the task
        self.status = status #Current status (todo, in-progress, done)
        self.createdAt = createdAt #Date and time of creation
        self.updatedAt = updatedAt #Date and time of last update

Tasks = []


def addTask(id, description, status, createdDate, updatedDate): #Add a task method
    task = Task(id, description, status, createdDate, updatedDate)
    Tasks.append(task)

def deleteTask(id): #Delete task method
    for task in Tasks:
        if task.id == id:
            Tasks.remove(task)

def updateTask(id):
    for task in Tasks:
        if task.id == id:
            print(task.description)
            task.description = input("Write the updated description ")

def printTasks(): #Print all tasks and their attributes
    if not Tasks:
        print("There are no tasks") 
    for task in Tasks:
        print ("ID: ", task.id)
        print ("Description: ", task.description)
        print ("Status: ", task.status)
        print ("Created: ", task.createdAt)
        print ("Modified: ", task.updatedAt)
    


addTask(input("ID "),input("Description "),input("status "),date.today(), date.today()) #Test input
os.system("clear")
printTasks()
updateTask(input("ID ")) #Test input
os.system("clear")
printTasks()
deleteTask(input("ID ")) #Test input
os.system("clear")
printTasks()