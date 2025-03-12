# ToDoList

A simple command-line task manager that allows users to add, view, and delete tasks, while ensuring secure and persistent storage with encryption.

## Features

- Add tasks
- View tasks
- Delete tasks
- Encrypted storage using `tasks.json`
- Secure key management using OS key storage

## Installation

Ensure you have **Python 3** installed on your system.

Clone the repository or download the script.

```sh
git clone <repository_url>
cd <repository_folder>
```

Install the required dependencies:

```sh
pip install cryptography keyring
```

## Usage

Run the script using Python:

```sh
python3 ToDoList.py
```

### Options:

1. **Add Task** - Prompts the user to enter a task and saves it.
2. **View Tasks** - Displays the list of saved tasks.
3. **Delete Task** - Allows the user to remove a task by its index.
4. **Exit** - Encrypts and saves the tasks securely, then exits the program.

## Security & Encryption

- Tasks are **encrypted** before being stored in `tasks.json`.
- The encryption key is **securely stored** using the OS keyring (`keyring` library).
- If the encryption key is not found, a **new key is generated and stored securely**.
- The key is **not pushed to Git** for added security.

## File Structure

- `tasks.json`: Stores the list of encrypted tasks persistently.
- `ToDoList.py`: Main script handling task management with encryption.

## How It Works

- When the script starts, it **retrieves or generates an encryption key** stored securely in the OS keyring.
- If `tasks.json` exists, it **decrypts the stored data** and loads the tasks.
- The user can **add, view, or delete tasks** through the command-line menu.
- Upon exiting, tasks are **encrypted and saved** back to `tasks.json`.

## Example

```sh
📌 To-Do List Menu:
1. ➕ Add task
2. 📜 View tasks
3. ❌ Delete task
4. 🚪 Exit
> 1
Enter the task: Buy groceries
> 2
0. Buy groceries
> 3
Enter the index of the task to remove: 0
> 2
📭 No tasks available!
```

## Contributing

Feel free to fork this repository and submit a pull request with improvements!

## License

This project is licensed under the Apache 2.0 License.

