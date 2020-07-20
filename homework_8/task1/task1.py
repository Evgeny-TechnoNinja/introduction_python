# Evgeny Baranov
# Homework 8


# ******************* task 1 (work file)
def read_file(name_file):
    try:
        with open(name_file, mode='r') as f:
            f_data = f.read()
            return f_data
    except FileNotFoundError:
        print(f'No "{name_file}" file') # noqa
        return


def write_file(input_data, mode, name_file='other.txt'):
    if input_data is None or input_data.isspace() or len(input_data) == 0:
        print('Can\'t work, empty data')
        return False
    else:
        with open(name_file, mode=mode) as f:
            f.write(input_data)
            return True


print('*********** Run: Task 1 ************')
result_data = read_file('example.txt')
print(result_data)

status_write = write_file(result_data, 'w', 'price.txt')
print(f'Write status {status_write}')

price_list = [int(current_value) for current_value in result_data.split()
              if current_value.isdigit()]
total_sum = sum(price_list)
write_file(f'Общая сумма: {total_sum}грн\n', 'a', 'example.txt')

# example of incorrect work
print('\n')
print(read_file('car.txt'))
status_write = write_file('        ', 'w')
print(f'Write status {status_write}')
print('*************************************')
# ***************************************
