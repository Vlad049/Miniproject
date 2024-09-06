def add_employee(employees: dict) -> dict:
    login = input("Введіть логін для користувача: ")
    position = input("Введіть посаду працівника: ")
    salary = input("Введіть заробітню плату для користувача: ")
    start_date = input("Введіть дату коли співробітник розпочав роботу. приклад: '01.01.2024': ")
    name = input("Введіть ім'я працівника: ")
    password = input("Введіть пароль для користувача: ")

    employees[login] = {
        "position": position,
        "salary": salary,
        "start_date": start_date,
        "name": name,
        "password": password
    }
    print("Користуча успішно додано.")

    return employees


def show_employees(emplyees: dict) -> None:
    for employee in emplyees:
        print(f"\nІнформація про користувача з логіном {employee}\n")
        for key, value in emplyees[employee].items():
            print(f"{key}: {value}")
    input("\n")


def del_employee(employees: dict) -> dict:
    login = input("Введіть логін співробітника, якого ви хочете видалити: ")

    if login in employees:
        del employees[login]
        print(f"Користувача '{login}' успішно видалено.")
    else:
        print("Такого користувача не знайдено.")
    return employees


def change_salary(employees: dict) -> dict:
    login = input("Введіть логін співробітника: ")

    if login in employees:
        salary = input("Введіть нове значення зарплати: ")
        employees[login]["salary"] = salary
        print("Суму ЗП успішно змінено")
    else:
        input("Такого користувача не знайдено")
    
    return employees


def change_position(employees: dict) -> dict:
    login = input("Введіть логін співробітника: ")

    if login in employees:
        position = input("Введіть нову посаду: ")
        employees[login]["position"] = position
        input("Посаду співробітника успішно змінено. Натисніть 'enter' для продовження ")
    else:
        input("Такого спіробітника не знайдено. Натисніть 'enter' для продовження ")
    
    return employees