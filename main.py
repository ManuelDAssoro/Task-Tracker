import tasks
import os
import datetime

def main():
    option = 0
    print("Welcome to Task Tracker!")
    while (option != 10):
        print("Menu - Enter the option number you want to execute \n 1: Add a task \n 2: Delete a task \n 3: Update a task \n 4: Mark a task as in progress \n 5: Mark a task as done \n 6: List all tasks \n 7: List all tasks that are done \n 8: List all tasks that are not done \n 9: List all tasks that are in progress \n 10: Exit")
        while(option <1 or option >10):
            option = int(input("Option: "))
        match option:
            case 1:
                tasks.addTask()
            case 2:
                id = input("ID: ")
                tasks.deleteTask(id)
            case 3:
                id = input("ID: ")
                tasks.updateTask(id)
            case 4:
                id = input("ID: ")
                tasks.markInProgress(id)
            case 5:
                id = input("ID: ")
                tasks.markDone(id)
            case 6:
                tasks.printTasks()
            case 7:
                tasks.printDoneTasks()
            case 8:
                tasks.printToDoTasks()
            case 9:
                tasks.printInProgressTasks()
            case 10:
                print("Keep on tracking!")