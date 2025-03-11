# ToDoList

A simple command-line task manager that allows users to add, view, and delete tasks, while saving them persistently in a JSON file.

## Features

- Add tasks
- View tasks
- Delete tasks
- Persistent storage using `tasks.json`

## Installation

Ensure you have **Python 3** installed on your system.

Clone the repository or download the script.

```sh
 git clone <repository_url>
 cd <repository_folder>
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
4. **Exit** - Saves the tasks to `tasks.json` and exits the program.

## File Structure

- `tasks.json`: Stores the list of tasks persistently.
- `ToDoList.py`: Main script handling task management.

## How It Works

- When the script starts, it **loads tasks** from `tasks.json` if it exists.
- User can **add, view, or delete tasks** through the command-line menu.
- When exiting, the script **saves tasks** back to `tasks.json`, creating it if it doesn't exist.

## Example

```
Select an option:
1. Add task
2. View tasks
3. Delete task
4. Exit
> 1
Enter the task: Buy groceries
> 2
0. Buy groceries
> 3
Enter the index of the task to remove: 0
> 2
There are no tasks
```

## Contributing

Feel free to fork this repository and submit a pull request with improvements!

## License

This project is licensed under the MIT License.

