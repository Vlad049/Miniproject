def add_animal(animals: list) -> list: #додаємо тварину
    animal = input("Додайте нову тваринку, якій необхідне лікування: ")

    if animal in animals:
        print("Ця тваринка вже записана на лікування!")
    else:
        animals.append(animal)
        print("Вашу тваринку додано!")

    return animals


def animal_cured(animals: list, animals_cured: list) -> tuple[list]:
    animal = input("Введіть ім'я тваринки, яку вже вилікувано: ")
    animals_lower = [animal.lower() for animal in animals]
    if animal.lower() in animals_lower:
        animals.remove(animal.lower().title())
        animals_cured.append(animal.lower().title())
        print(f"Тваринку '{animal}' вилікувано")
    else:
        print(f"Тваринка '{animal}' відсутня в списку")

    return animals, animals_cured


def show_all_cured_animals(animals_cured: list) -> None:
    print("Список тваринок, яких вилікували:")
    for i, animal in enumerate(animals_cured, start=1):
        print(f"{i}: {animal}")


def show_all_animals(animals: list) -> None:
    delimiter = "-" * 23
    template = "|{:<9}|{:>11}|"

    print(delimiter)
    for i, animal in enumerate(animals, start=1):
        print(template.format(i, animal))
    print(delimiter)


def delete_animal(animals: list) -> list:
    animal = input("Введіть ім'я тваринки, яку ви хочете видалити: ")

    if animal in animals:
        animals.remove(animal)
        print(f"Тваринку '{animal}' видалено зі списку")
    else:
        print(f"Тваринка '{animal}' відсутня в списку")

    return animals


def find_palindrom(animals: list) -> None:
    palindrom_pet = []
    for animal in animals:
        if animal.lower() == animal.lower()[::-1]:
            palindrom_pet.append(animal)

    print(f"Тваринки з ім'ям паліндромом: {palindrom_pet}")
