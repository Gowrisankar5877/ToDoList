<H1>Git and GitHub Case Study: To-Do List Application</H1>
<br>
<H2>Project Overview</H2>
<br>
<p>This repository contains a simple Python-based To-Do List application, developed as part of a Git and GitHub case study assignment. The application allows users to manage tasks effectively by adding, deleting, and marking tasks as complete. Users can also categorize tasks by priority or due date.</p>
<br>
<p>This project demonstrates proficiency in using Git and GitHub for version control, collaboration, and best practices such as branching, merging, tagging, and creating hooks.</p>

<H3>Features</H3>
  1. Add new tasks with a title, description, priority, and due date.
  2. Mark tasks as complete.
  3. Filter tasks by priority.
  4. View all tasks in the list.
  5. Delete tasks when no longer needed.
<H3>Technology Stack</H3>
<B>Language:</B> Python
<B>Tools/Technologies:</B> Git, GitHub
<B>Dependencies:</B> flake8 (for code style checking)
<br>
<b>Project Structure</b>

ToDoList/
│
├── main.py                # Main entry point of the application
├── task.py                # Task class to represent individual tasks
├── task_manager.py        # TaskManager class for managing tasks
├── README.md              # Project documentation
├── .gitignore             # Files and directories to ignore in Git
├── hooks/
│   ├── pre-commit         # Pre-commit hook to check code style
└── .git/                  # Git repository data
<H3>Setup and Installation</H3>
<b>Clone the repository:</b>
git clone git@github.com:<YourUsername>/ToDoList.git
cd ToDoList
<b>Install required dependencies:</b>
pip install flake8
<b>Set up Git hooks:</b>
<b>Pre-Commit Hook:</b> Copy the pre-commit script into .git/hooks and make it executable:
cp hooks/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit

<b>Run the application:</b>
  python main.py
<b>Using the Application</b>
<b>Add a Task:</b> Enter task details like title, description, priority, and due date.
<b>Mark a Task as Completed:</b> Update the task's status to "Completed."
<b>View All Tasks:</b> Display the list of tasks along with their status and priority.
<b>Filter Tasks:</b>Filter tasks based on their priority (e.g., High, Medium, Low).
<b>Delete a Task:</b> Remove a task from the list.

<h3>Git Workflow and Best Practices</h3>

<b>Branching:</b>

feature/initial-development for core functionality.
feature/test for testing new features.
bugfix/issue-1 for fixing bugs.
feature/new-ui for major UI redesign.
Commit Messages: Meaningful and concise commit messages for traceability 

Collaboration: Pull requests created for each feature/bugfix branch, reviewed, and merged into main.


<b>Tagging:</b>

Tag v1.0 created for the initial release.
Pre-Commit 
Pre-Commit Hook: Ensures Python code adheres to style guidelines using flake8.
