# To-Do List

A simple command-line To-Do List application written in Python. This program allows users to add, view, complete, and delete tasks. Tasks are stored in a text file so they can be saved and accessed later.

## Features

* Add one or multiple tasks
* View all saved tasks
* Mark tasks as completed
* Delete tasks
* Store tasks in a text file
* Simple command-line interface

## How to Run

### Requirements

* Python 3.x

### Steps

1. Clone or download this project.
2. Open the project folder in your terminal or VS Code.
3. Run the Python program:

```bash
python todo.py
```

> Replace `todo.py` with the actual name of your Python file if it is different.

## How to Use

When the program starts, you will see the following menu:

```text
===== TO-DO LIST =====
1. Add task
2. View tasks
3. Mark task as completed
4. Delete task
5. Exit
```

### 1. Add Task

Select `1` and enter your task.

Example:

```text
Enter your task: Complete Python project
Do you want to add more tasks (yes/no)? no
```

The task will be saved in `task.txt`.

### 2. View Tasks

Select `2` to display all saved tasks.

Example:

```text
Complete Python project
Learn file handling
Practice Python
```

### 3. Mark Task as Completed

Select `3` and enter the exact task you completed.

Example:

```text
Enter the task you completed: Complete Python project
```

The task will be changed to:

```text
[Completed]Complete Python project
```

### 4. Delete Task

Select `4` and enter the task you want to remove.

The task will then be deleted from `task.txt`.

### 5. Exit

Select `5` to close the program.

```text
Goodbye!
```

## Technologies Used

* Python
* File Handling
* Functions
* Loops
* Conditional Statements
* User Input

## Future Improvements

Some possible improvements for future versions:

* Add task IDs/numbers
* Add due dates
* Add task priorities
* Allow users to edit tasks
* Improve the completed-task formatting
* Handle the case when `task.txt` does not exist
* Add a confirmation before deleting a task
* Separate completed and pending tasks

