# Evgeny Baranov
# Homework 12

import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем и возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def hack_archive(file_name):
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    def generate_num(num_start, num_end, row_length):
        str_result = ''
        list_sing = [str(v) for v in range(num_start, num_end)]
        for i in range(row_length):
            random_sing = random.sample(list_sing, 1)
            str_result += ''.join(random_sing)
        return str_result

    while True:
        password = generate_num(0, 10, PASSWORD_LENGTH)
        if password not in wrong_passwords:
            process_result = extract_archive(file_to_open, password)
            if process_result:
                break
            else:
                tries += 1
                wrong_passwords.append(password)

    print(f'Archive {file_name} is hacked. Password - {password}') # noqa
    print(f'Password was found after {tries} tries')


#############
filename = 'task.zip'
hack_archive(filename)
