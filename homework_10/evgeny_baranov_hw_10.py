# Evgeny Baranov
# Homework 10

from datetime import datetime as dt


# ******************* task 1 (date formatting)
def formatting_datetime(str_datetime):
    try:
        return dt.strptime(str_datetime, "%b %d %Y %I:%M%p")
    except ValueError:
        print('The input string does not match the format!')
    except TypeError:
        print('Working with a string in the correct format')
    return


str_date_example_one = 'Feb 12 2019 2:41PM'
str_date_example_two = 'Apr 01 2018 1:11AM'
# different format
str_date_example_three = '01 Feb 2017 3:20AM'
str_date_example_four = '20 05 2020 22:20:10'
sing_num = 20062019120059
print('*********** Run: Task 1 ************')
print(formatting_datetime(str_date_example_one))
print(formatting_datetime(str_date_example_two))
# error
print(formatting_datetime(str_date_example_three))
print(formatting_datetime(str_date_example_four))
print(formatting_datetime(sing_num))
print('************************************')
# *****************************************
print('\n')


# ******************* task 2 (prime number)
def is_prime(custom_num):
    if isinstance(custom_num, int):
        if custom_num in [0, 1]:
            return False
        else:
            div_count = 0
            for current_num in range(1, custom_num + 1):
                if custom_num % current_num == 0:
                    div_count += 1
                    if div_count > 2:
                        return False
            return True
    else:
        print('Работаю только с числами!')


print('*********** Run: Task 2 ************')
# True
print(is_prime(5))
print(is_prime(13))
print(is_prime(29))
print(is_prime(211))
# False
print(is_prime(1))
print(is_prime(4))
print(is_prime(6))
print(is_prime(20))
# Error
print(is_prime('spam'))
print('************************************')
# *****************************************
print('\n')


# ******************* task 3 (parse)
def parse(custom_str):
    if isinstance(custom_str, str):
        init_value = 0
        result = []
        for current_value in custom_str.lower():
            if current_value == 'i':
                init_value += 1
            elif current_value == 'd':
                init_value -= 1
            elif current_value == 's':
                init_value = init_value ** 2
            elif current_value == 'o':
                result.append(init_value)
        return result
    else:
        print('Работаю только со строками')


print('*********** Run: Task 3 ************')
print(parse('iiisdoso'))
print(parse('iso'))
print(parse('Most good programmers do their job not because '
            'they expect payment or recognition, '
            'but because they enjoy programming.'))
print(parse('Any fool can write code that the machine can understand. '
            'Good programmers write code that humans can understand.'))
print(parse('Testing does not detect bugs such as creating the wrong application.')) # noqa
# not fit
print(parse(123))
print(parse(['spam', 'bob']))
print('************************************')
