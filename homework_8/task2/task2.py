# Evgeny Baranov
# Homework 8

import json


# ******************* task 2
QUESTIONS_LIST = []
ANSWERS_LIST = []
KEY_STR = None
JSON_FILE = 'questions.json'


def get_reformed_json(json_file_name):
    try:
        with open(json_file_name, mode='r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'No "{json_file_name} file"') # noqa
        return


def set_data_json(json_file_name, obj_file_name):
    with open(json_file_name, mode='w') as f:
        json.dump(obj_file_name, f, indent=4)


def fill_questions(obj_data, obj_key, result_list):
    temp_list = obj_data[obj_key]
    for current_value in temp_list:
        for current_set in current_value.items():
            if len(current_set[1]) > 0:
                result_list.append(current_set[1])
    return result_list


def questionnaire(input_list, result_list):
    for current_value in input_list:
        current_answer = input(f'{current_value}> ')
        result_list.append(current_answer)
    return result_list


def suitability_check(obj_list):
    for current_value in obj_list:
        if len(current_value) == 0 or current_value.isspace():
            return False
    return True


def field_check(obj_data, obj_key):
    for current_value in obj_data[obj_key]:
        temp_keys_list = current_value.keys()
        for current_key in temp_keys_list:
            temp_value = current_value.get(current_key)
            if len(temp_value) == 0:
                return True
    return False


def add_data(obj_data, obj_key, obj_answer):
    count = 0
    for current_value in obj_data[obj_key]:
        temp_keys_list = current_value.keys()
        for current_key in temp_keys_list:
            temp_value = current_value.get(current_key)
            if len(temp_value) == 0:
                current_value[current_key] = obj_answer[count]
                count += 1
    if count == len(obj_answer):
        return True
    else:
        return False


def main():
    global QUESTIONS_LIST, ANSWERS_LIST, KEY_STR, JSON_FILE
    data_dict = get_reformed_json(JSON_FILE)
    if data_dict is None:
        print('Can not work, no data')
    else:
        KEY_STR = list(data_dict.keys())[0]
        if field_check(data_dict, KEY_STR):
            fill_questions(data_dict, KEY_STR, QUESTIONS_LIST)
        else:
            print('The fields are already filled!')
    if len(QUESTIONS_LIST) > 0:
        print('Warning: Be sure to answer all questions')
        questionnaire(QUESTIONS_LIST, ANSWERS_LIST)
        if suitability_check(ANSWERS_LIST):
            if add_data(data_dict, KEY_STR, ANSWERS_LIST):
                set_data_json(JSON_FILE, data_dict)
                print('Success: The questionnaire is completed')
            else:
                print('No data has been written, the field may not be empty!')
        else:
            print('The data is filled in incompletely or incorrectly')
    else:
        print('Can not work, no data')


if __name__ == '__main__':
    main()

# *************************
