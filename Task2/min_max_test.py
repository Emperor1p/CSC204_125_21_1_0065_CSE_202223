# main.py
from min_max import SingleLinkedList


if __name__ == "__main__":
    print("Testing min value and max value:")


    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    linked_list = SingleLinkedList()

    for data in data_list:
        linked_list.insert(data)

    linked_list.display()

    # Test find_min_max method
    min_val, max_val = linked_list.find_min_max()
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")

