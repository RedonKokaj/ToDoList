import os
import json

task_list = []
file_path = os.path.join(os.path.dirname(__file__), "tasks.json")


def loadTasks():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            global task_list
            task_list = json.load(file)


def saveTasks():
    with open(file_path, "w") as file:
        json.dump(task_list, file)


def addTask():
    task = input("Enter the task: ")
    task_list.append(task)


def deleteTask():
    if not task_list:
        print("There are no tasks")
        return
    viewTask()
    index = int(input("Enter the index of the task to remove: "))
    if 0 <= index < len(task_list):
        task_list.pop(index)
    else:
        print("Invalid index")


def viewTask():
    if not task_list:
        print("There are no tasks")
        return
    for index, task in enumerate(task_list):
        print(f"{index}. {task}")


def main():
    loadTasks()
    try:
        while True:
            print("Select an option:")
            print("1. Add task")
            print("2. View tasks")
            print("3. Delete task")
            print("4. Exit")
            choice = int(input())
            print("--------------------")
            if choice == 1:
                addTask()
            elif choice == 2:
                viewTask()
            elif choice == 3:
                deleteTask()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
            print("--------------------")
    finally:
        saveTasks()


if __name__ == "__main__":
    main()
