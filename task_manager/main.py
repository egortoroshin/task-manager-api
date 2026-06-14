tasks = []

def add_task(title):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    print(f"Задача '{title}' добавлена!")

def show_tasks():
    if len(tasks) == 0:
        print("Нет задач.")
        return
    for task in tasks:
        status = "✓" if task["done"] else "○"
        print(f"[{status}] {task['id']}. {task['title']}")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Задача '{task['title']}' выполнена!")
            return
    print(f"Задача с id {task_id} не найдена.")

def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Задача '{task['title']}' удалена!")
            return
    print(f"Задача с id {task_id} не найдена.")

def menu():
    while True:
        print("\n--- Менеджер задач ---")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Выполнить задачу")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название задачи: ")
            add_task(title)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_id = int(input("Введите id задачи: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Введите id задачи: "))
            delete_task(task_id)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

menu()