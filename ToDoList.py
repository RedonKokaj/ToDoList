import os
import json
import keyring
from cryptography.fernet import Fernet

# Constants
SERVICE_NAME = "ToDoApp"  # Name for OS key storage
TASK_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


# Load or generate encryption key
def get_encryption_key():
    key = keyring.get_password(SERVICE_NAME, "encryption_key")
    if key is None:
        key = Fernet.generate_key().decode()  # Generate new key
        keyring.set_password(SERVICE_NAME, "encryption_key", key)
        # print("🔑 New encryption key generated and stored securely!")
    return key.encode()


# Encrypt and decrypt functions
def encrypt_data(data, key):
    return Fernet(key).encrypt(json.dumps(data).encode())


def decrypt_data(encrypted_data, key):
    try:
        return json.loads(Fernet(key).decrypt(encrypted_data).decode())
    except:
        print("❌ Error: Unable to decrypt data. Is the correct key stored?")
        return []


# Save encrypted tasks
def save_tasks():
    key = get_encryption_key()
    encrypted_data = encrypt_data(task_list, key)
    with open(TASK_FILE, "wb") as file:
        file.write(encrypted_data)


# Load and decrypt tasks
def load_tasks():
    global task_list
    if os.path.exists(TASK_FILE):
        key = get_encryption_key()
        with open(TASK_FILE, "rb") as file:
            encrypted_data = file.read()
        task_list = decrypt_data(encrypted_data, key)


# Task operations
def add_task():
    task = input("Enter the task: ")
    task_list.append(task)


def delete_task():
    if not task_list:
        print("❌ No tasks available!")
        return
    view_tasks()
    try:
        index = int(input("Enter the index of the task to remove: "))
        if 0 <= index < len(task_list):
            task_list.pop(index)
        else:
            print("❌ Invalid index")
    except ValueError:
        print("❌ Please enter a valid number")


def view_tasks():
    if not task_list:
        print("📭 No tasks available!")
        return
    for index, task in enumerate(task_list):
        print(f"{index}. {task}")


# Main program loop
def main():
    load_tasks()
    try:
        while True:
            print("\n📌 To-Do List Menu:")
            print("1. ➕ Add task")
            print("2. 📜 View tasks")
            print("3. ❌ Delete task")
            print("4. 🚪 Exit")
            choice = input("Enter your choice: ")
            print("--------------------")

            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                break
            else:
                print("❌ Invalid choice. Please try again.")
            print("--------------------")
    finally:
        save_tasks()


if __name__ == "__main__":
    task_list = []
    main()
