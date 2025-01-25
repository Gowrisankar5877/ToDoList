from task import Task
from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    
    while True:
        print("\n--- ToDo List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View All Tasks")
        print("4. Filter by Priority")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low/Medium/High): ") or "Medium"
            due_date = input("Enter task due date (YYYY-MM-DD, optional): ")
            task = Task(title, description, priority, due_date)
            task_manager.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            title = input("Enter the title of the task to remove: ")
            task_to_remove = next((task for task in task_manager.get_all_tasks() if task.title == title), None)
            if task_to_remove:
                task_manager.remove_task(task_to_remove)
                print("Task removed successfully!")
            else:
                print("Task not found.")
        elif choice == '3':
            tasks = task_manager.get_all_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")
        elif choice == '4':
            priority = input("Enter priority to filter by (Low/Medium/High): ")
            filtered_tasks = task_manager.filter_by_priority(priority)
            if filtered_tasks:
                print("\nFiltered Tasks:")
                for task in filtered_tasks:
                    print(task)
            else:
                print("No tasks found with the given priority.")
        elif choice == '5':
            title = input("Enter the title of the task to mark as completed: ")
            task_to_mark = next((task for task in task_manager.get_all_tasks() if task.title == title), None)
            if task_to_mark:
                task_manager.mark_task_completed(task_to_mark)
                print("Task marked as completed!")
            else:
                print("Task not found.")
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
