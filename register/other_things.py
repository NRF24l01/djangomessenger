import re


def is_valid_email(email):
    # Регулярное выражение для проверки формата адреса
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Проверка формата адреса
    if re.match(pattern, email):
        return True
    else:
        return False
