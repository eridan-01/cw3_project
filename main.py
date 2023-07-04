from utils import get_data, delete_empty_operations, get_first_five_sorted_operations, print_list_operation
from settings import PATH_WITH_FIXTURES


def main():
    data = get_data(PATH_WITH_FIXTURES)
    new_data = delete_empty_operations(data)
    five_operations = get_first_five_sorted_operations(new_data)
    end_ = print_list_operation(five_operations)
    print(end_)


if __name__ == '__main__':
    main()
