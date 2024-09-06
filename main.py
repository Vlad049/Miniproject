from datetime import datetime
from pprint import pprint

from src.password import generate_password
from src.animals import (
    show_all_animals,
    add_animal,
    animal_cured,
    show_all_cured_animals,
    delete_animal,
    find_palindrom
)
from src.reviews import (
    write_review,
    show_all_reviews,
    find_repeated_phrases
)
from src.employees import (
    add_employee,
    del_employee,
    show_employees,
    change_salary,
    change_position
)

from files.list_files import HELP
from src import files_actions


def help(path: str = HELP):
    with open(path, "r", encoding="utf-8") as file:
        print(file.read())


def leave():
    print("Дякуємо, що скористалися нашою вет-клінікою. До нових зустрічей!.")
    quit()


def show_log(log: list) -> None:
    pprint(log, width=230)


def main():
    animals = files_actions.open_animals()
    animals_cured = files_actions.open_animals_cured()
    reviews = files_actions.open_reviews()
    log = files_actions.open_log()
    employees = files_actions.open_employees()
    login_global = input("Введіть свій логін користувача: ")
    password = employees.get(login_global, {}).get("password")
    if not password:
        position = input("Введіть свою посаду: ")
        salary = input("Введіть свою зарплату: ")
        name = input("Введіть своє ім'я: ")
        start_date = datetime.now().strftime("%d.%m.%Y")

        employees[login_global] = {
            "position": position,
            "salary": salary,
            "start_date": start_date,
            "name": name,
            # "password" : PASSWORD
        }
        
        password = generate_password()
        employees[login_global]["password"] = password

    else:
        input(f"Пароль створено: '{password}'. Запам'ятайте його. Введіть Enter для продовження  ")

    password_global = input("Введіть пароль для входу у систему: ")

    command = ""
    while password_global == password:
        if not command:
            log.append(f"Користувач з логіном {login_global} зайшов у систему о {datetime.now()}")
            print("Доброго дня, вітаємо у нашій вет клінці")

        command = input("\nВведіть код команди, або введіть 'help' для показу всіх команд: ")
        log.append(f"Користувач з логіном {login_global} ввів команду {command} о {datetime.now()}")

        match command:
            case "show all animals":
                show_all_animals(animals)
            case "add animal":
                animals = add_animal(animals)
            case "animal cured":
                animals, animals_cured = animal_cured(animals, animals_cured)
            case "show all cured animals":
                show_all_cured_animals(animals_cured)
            case "leave":
                files_actions.save_animals(animals)
                files_actions.save_animals_cured(animals_cured)
                files_actions.save_reviews(reviews)
                files_actions.save_employees(employees)
                files_actions.save_log(log)
                leave()
            case "delete animal":
                animals = delete_animal(animals)
            case "write review":
                reviews = write_review(reviews)
            case "show all reviews":
                show_all_reviews(reviews)
            case "find repeated prases":
                find_repeated_phrases(reviews)
            case "find palindrom":
                find_palindrom(animals)
            case "add employee":
                employees = add_employee(employees)
            case "del employee":
                employees = del_employee(employees)
            case "show employees":
                show_employees(employees)
            case "change salary":
                employees = change_salary(employees)
            case "change position":
                employees = change_position(employees)
            case "show log":
                show_log(log)
            case "help":
                help()
            case _:
                print("Такої команди не знайдено. Спробуйте ще раз")
    else:
        print("Пароль не правильний. Доступ заблокований")

if __name__ == "__main__":
    main()