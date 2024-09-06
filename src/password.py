def is_verify_password(password:str) -> bool:
    if len(password) >= 8:
        is_len_pass = True
    else:
        is_len_pass = False

    is_have_digit = False
    is_have_char = False

    for char in password:
        if char.isalpha():
            is_have_char = True
        elif char.isdigit():
            is_have_digit = True

    if is_len_pass and is_have_digit and is_have_char:
        return True
    else:
        return False


def generate_password() -> str:
    while True:
        command = input("Необхідно створити пароль для користування системою! Натисніть '1' для продовження. Натисніть '2' для виходу з програми: ")

        if command == "1":
            password = input("Введіть свій пароль. Довжина паролю має бути мінімум 8 символів та містити мінімум одну літеру та одну цифру: ")

            if is_verify_password(password):
                return password
            else:
                input("Ваш пароль не відповідає умовам, спробуйте ще раз. Для продовження натисніть Enter")
        
        elif command == "2":
            quit()
