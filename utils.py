import json
import datetime


def get_data(path):
    with open(path) as file:
        return json.load(file)


def delete_empty_operations(operations):
    operations.remove({})
    return operations


def get_first_five_sorted_operations(list_operations):
    return sorted(
        list_operations,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]


def convert_date(date):
    date_ = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.datetime.strftime(date_, '%d.%m.%Y')


def convert_number_to(number):
    if not number:
        return
    elif number.startswith('Счет'):
        date = number.split(' ')
        number_two_ = date.pop(-1)
        return f'{" ".join(date)} **{number_two_[-4:]}'
    else:
        date = number.split(' ')
        numbers = date.pop(-1)
        number_ = ' '.join([number[i:i + 4] for i in range(0, len(numbers), 4)])
        return f'{" ".join(date)} {number_[:7]} **** {number_[-4:]}'


def convert_number_from(number_two: str):
    if not number_two:
        return
    elif number_two.startswith('Счет'):
        date = number_two.split(' ')
        number_two_ = date.pop(-1)
        return f'{" ".join(date)} **{number_two_[-4:]}'
    else:
        date = number_two.split(' ')
        number = date.pop(-1)
        number_ = ' '.join([number[i:i+4] for i in range(0, len(number), 4)])
        return f'{" ".join(date)} {number_[:7]} **** {number_[-4:]}'


def print_list_operation(list_operation):
    for list_ in list_operation:
        print(f'{convert_date(list_["date"])} {list_["description"]}\n{convert_number_from(list_.get("from"))} -> {convert_number_to(list_["to"])}\n{list_["operationAmount"]["amount"]} {list_["operationAmount"]["currency"]["name"]}\n')
    return ""
