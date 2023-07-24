# main.py
from linkedlist import SingleLinkedList

def test_single_linked_list():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    linked_list = SingleLinkedList()

    for data in data_list:
        linked_list.insert(data)

    linked_list.display()

if __name__ == "__main__":
    print("Testing Single Linked List:")
    test_single_linked_list()
