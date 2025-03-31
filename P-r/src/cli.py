from src.models.todo_list import ToDoList
from src.storage.file_storage import FileStorage

def main():
    todo_list = ToDoList()
    storage = FileStorage()
    
    todo_list.tasks = storage.load_tasks()
    
    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list.get_tasks(), 1):
            print(f"{i}. {task}")

        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task completed")
        print("4. Save & Exit")
        print("5. Show Todo_list")

        choice = input("Choose an option: ")
        
        if choice == "1":
            desc = input("Enter task: ")
            try:
                todo_list.add_task(desc)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            desc = input("Enter task to remove: ")
            try:
                todo_list.remove_task(desc)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            desc = input("Enter task to mark completed: ")
            try:
                todo_list.mark_task_completed(desc)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            storage.save_tasks(todo_list.get_tasks())
            print("Tasks saved. Exiting...")
            break
        elif choice == "5":
            j = 1
            for i in todo_list.get_tasks():
                print(f'{j} - {i}')
                j +=1
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
