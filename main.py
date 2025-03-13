import tasks #Import tasks module
import os
import os.path
import datetime

def main():
    path = '/home/manuel/roadmap/Tasks.json' #Define path as the Task's file path
    if os.path.exists(path): #Check if path exist, if it doesn't create it
        print("Loading your Task list!")
        tasks.loadTasks()
    else:
        print("No task list found! Creating a new one...")
        tasks.saveTasks()
    option = 0
    print("Welcome to Task Tracker!")
    while (option != 10):
        print("Menu - Enter the option number you want to execute \n 1: Add a task \n 2: Delete a task \n 3: Update a task \n 4: Mark a task as in progress \n 5: Mark a task as done \n 6: List all tasks \n 7: List all tasks that are done \n 8: List all tasks that are not done \n 9: List all tasks that are in progress \n 10: Exit")
        while(option <1 or option >10):
            option = int(input("Option: "))
        match option:
            case 1:
                tasks.addTask()
                option = 0
            case 2:
                id = input("ID: ")
                tasks.deleteTask(id)
                option = 0
            case 3:
                id = input("ID: ")
                tasks.updateTask(id)
                option = 0
            case 4:
                id = input("ID: ")
                tasks.markInProgress(id)
                option = 0
            case 5:
                id = input("ID: ")
                tasks.markDone(id)
                option = 0
            case 6:
                tasks.printTasks()
                input("\nPress Enter to continue...")
                option = 0
            case 7:
                tasks.printDoneTasks()
                input("\nPress Enter to continue...")
                option = 0
            case 8:
                tasks.printToDoTasks()
                input("\nPress Enter to continue...")
                option = 0
            case 9:
                tasks.printInProgressTasks()
                input("\nPress Enter to continue...")
                option = 0
            case 10:
                os.system('clear')
                print("Thanks for using Task Tracker!")      

main()