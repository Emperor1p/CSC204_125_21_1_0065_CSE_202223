# linkedlists/single_linked_list.py
from node import Node 

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def find_min_max(self):
        if not self.head:
            return None, None

        data_list = []
        current_node = self.head
        while current_node:
            data_list.append(current_node.data)
            current_node = current_node.next_node

        data_list.sort()
        return data_list[0], data_list[-1]

