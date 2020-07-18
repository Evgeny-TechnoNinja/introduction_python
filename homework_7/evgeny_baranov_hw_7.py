# Evgeny Baranov
# Homework 7


# ******************* task 1 (season)
def get_season(number):
    months = ('Winter', 'Spring', 'Summer', 'Autumn')
    notice = 'The month numbered'
    if number in [12, 1, 2]:
        return f'{notice} {number} {months[0]}' # noqa
    elif number in [3, 4, 5]:
        return f'{notice} {number} {months[1]}'
    elif number in [6, 7, 8]:
        return f'{notice} {number} {months[2]}'
    elif number in [9, 10, 11]:
        return f'{notice} {number} {months[3]}'
    else:
        return 'I can not process the data'


print('*********** Run: Task 1 ************')
print(get_season(1))
print(get_season(5))
print(get_season(8))
print(get_season(7))
print(get_season(11))
print(get_season(''))
print(get_season('a'))
print(get_season([]))
print('************************************')
# *****************************************
print('\n')


# ******************* task 2 ( dict, word quantity)
def converter(string, separator):
    list_temp = string.split(separator)
    i = 0
    while i < len(list_temp):
        list_temp[i] = list_temp[i].strip()
        i += 1
    dict_results = dict.fromkeys(list_temp, 0)
    for current_key_dict in dict_results.keys():
        for current_value_list in list_temp:
            if current_value_list == current_key_dict:
                dict_results[current_key_dict] += 1
    return dict_results


print('*********** Run: Task 2 ************')
while True:
    my_str = input('Enter string >')
    if len(my_str) > 0:
        break
    else:
        print('Please enter some text')
while True:
    delimiter = input('Enter delimiter >')
    if len(delimiter) > 0:
        break
    else:
        print('Please enter delimiter')

print(converter(my_str, delimiter))
print('************************************')
# ******************************************
print('\n')


# ******************* task 3 (square)
def get_rectangle_data(a):
    if isinstance(a, (int, float)):
        sqr_two = 1.414
        d = a * sqr_two
        s = a * a
        p = a * 4
        return f'Perimeter of square P = ' \
                f'{("%.3f" % p) if isinstance(p, float) else p}\n' \
                f'Area of square S = ' \
                f'{("%.3f" % s) if isinstance(s, float) else s}\n' \
                f'Diagonal of square d = ' \
                f'{("%.3f" % d) if isinstance(d, float) else d}'
    else:
        return 'Only work with numbers!'


print('*********** Run: Task 3 ************')
print(get_rectangle_data(6))
print('\n')
print(get_rectangle_data(3))
print('\n')
print(get_rectangle_data(2))
print('\n')
print(get_rectangle_data(2.5))
print('\n')
print(get_rectangle_data(9.99))
print('\n')
print(get_rectangle_data('abc'))
print('************************************')
# ***********************************
