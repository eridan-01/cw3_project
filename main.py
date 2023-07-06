from settings import PATH_WITH_FIXTURES
from utils import get_data, delete_empty_operations, get_first_five_sorted_operations, get_results


def main():
    data = get_data(PATH_WITH_FIXTURES)
    new_data = delete_empty_operations(data)
    five_operations = get_first_five_sorted_operations(new_data)
    print_list_operation = get_results(five_operations)
    print(print_list_operation)


if __name__ == '__main__':
    main()
