from settings import PATH_WITH_FIXTURES
from utils import get_data, delete_empty_operations, get_first_five_sorted_operations, print_list_operation, convert_date

data = get_data(PATH_WITH_FIXTURES)
new_data = delete_empty_operations(data)
five_operations = get_first_five_sorted_operations(new_data)
end_ = print_list_operation(five_operations)


def test_get_data():
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


def test_get_first_five_sorted_operation():
    assert five_operations[1]['state'] == 'EXECUTED', "Операция не имеет статус 'EXECUTED'"
    assert len(five_operations) == 5


def test_convert_date():
    assert convert_date(five_operations[2]['date']) == '19.11.2019'
