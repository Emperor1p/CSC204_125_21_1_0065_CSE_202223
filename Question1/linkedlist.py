# linkedlists/single_linked_list.py
from node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None #the head will be empty since it is the starting point

    def insert(self, data):
        new_node = Node(data) #Node is the class name imported from the node file
        if not self.head: #when new node is not in the data in the node file then we need to add it to the head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head #here every node link to the head will be connected from one node to another
        while current_node:
            print(current_node.data, end=" -> ") #here we want to display those data linked to the head
            current_node = current_node.next_node
        print("None")


if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28] # data list of the data
    linked_list = SingleLinkedList()

    for data in data_list: # I used for loop to display them one after the other
        linked_list.insert(data)

    linked_list.display()

 