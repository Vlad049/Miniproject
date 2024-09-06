import os
import json

from files import list_files

if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.ANIMALS_CURED):
    with open(list_files.ANIMALS_CURED, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.EMPLOYEES):
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as file:
        json.dump({}, file)

if not os.path.exists(list_files.LOG):
    with open(list_files.LOG, "w", encoding="utf-8") as file:
        json.dump([], file)


def open_animals(path: str = list_files.ANIMALS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        animals = json.load(file)

    return animals


def save_animals(animals: list, path: str = list_files.ANIMALS) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(animals, file, ensure_ascii=False, indent=4)


def open_animals_cured(path: str = list_files.ANIMALS_CURED) -> list:
    with open(path, "r", encoding="utf-8") as file:
        animals_cured = json.load(file)

    return animals_cured


def save_animals_cured(animals_cured: list, path: str = list_files.ANIMALS_CURED) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(animals_cured, file, ensure_ascii=False, indent=4)


def open_reviews(path: str = list_files.REVIEWS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews


def save_reviews(reviews: list, path: str = list_files.REVIEWS) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(reviews, file, ensure_ascii=False, indent=4)


def open_employees(path: str = list_files.EMPLOYEES) -> dict[dict]:
    with open(path, "r", encoding="utf-8") as file:
        employees = json.load(file)

    return employees


def save_employees(employees: list, path: str = list_files.EMPLOYEES) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)


def open_log(path: str = list_files.LOG) -> list:
    with open(path, "r", encoding="utf-8") as file:
        log = json.load(file)

    return log


def save_log(log: list, path: str = list_files.LOG) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(log, file, ensure_ascii=False, indent=4)