<H1>Git and GitHub Case Study: To-Do List Application</H1>
<br>
<H2>Project Overview</H2>
<br>
<p>This repository contains a simple Python-based To-Do List application, developed as part of a Git and GitHub case study assignment. The application allows users to manage tasks effectively by adding, deleting, and marking tasks as complete. Users can also categorize tasks by priority or due date.</p>
<br>
<p>This project demonstrates proficiency in using Git and GitHub for version control, collaboration, and best practices such as branching, merging, tagging, and creating hooks.</p>

<H3>Features</H3>
  1. Add new tasks with a title, description, priority, and due date.<br>
  2. Mark tasks as complete.<br>
  3. Filter tasks by priority.<br>
  4. View all tasks in the list.<br>
  5. Delete tasks when no longer needed.<br>
<H3>Technology Stack</H3><br>
<B>Language:</B> Python<br>
<B>Tools/Technologies:</B> Git, GitHub<br>
<B>Dependencies:</B> flake8 (for code style checking)
<br>
<b>Project Structure</b>

ToDoList/<br>
│<br>
├── main.py                # Main entry point of the application<br>
├── task.py                # Task class to represent individual tasks<br>
├── task_manager.py        # TaskManager class for managing tasks<br>
├── README.md              # Project documentation<br>
├── .gitignore             # Files and directories to ignore in Git<br>
├── hooks/        <br>
│   ├── pre-commit         # Pre-commit hook to check code style<br>
└── .git/                  # Git repository data<br>
<H3>Setup and Installation</H3>
<b>Clone the repository:</b><br>
git clone git@github.com:<YourUsername>/ToDoList.git<br>
cd ToDoList<br>
<b>Install required dependencies:</b><br>
pip install flake8<br>
<b>Set up Git hooks:</b><br>
<b>Pre-Commit Hook:</b> Copy the pre-commit script into .git/hooks and make it executable:<br>
cp hooks/pre-commit .git/hooks/<br>
chmod +x .git/hooks/pre-commit<br>

<b>Run the application:</b><br>
  python main.py<br>
<b>Using the Application</b><br>
<b>Add a Task:</b> Enter task details like title, description, priority, and due date.<br>
<b>Mark a Task as Completed:</b> Update the task's status to "Completed."<br>
<b>View All Tasks:</b> Display the list of tasks along with their status and priority.<br>
<b>Filter Tasks:</b>Filter tasks based on their priority (e.g., High, Medium, Low).<br>
<b>Delete a Task:</b> Remove a task from the list.<br>

<h3>Git Workflow and Best Practices</h3>
<b>Branching:</b>
<br>
feature/initial-development for core functionality.<br>
feature/test for testing new features.<br>
bugfix/issue-1 for fixing bugs.<br>
feature/new-ui for major UI redesign.<br>
Commit Messages: Meaningful and concise commit messages for traceability <br>

Collaboration: Pull requests created for each feature/bugfix branch, reviewed, and merged into main.<br>


<b>Tagging:</b> <br>

Tag v1.0 created for the initial release.<br>
Pre-Commit <br>
Pre-Commit Hook: Ensures Python code adheres to style guidelines using flake8. 
