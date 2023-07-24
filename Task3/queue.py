class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    def sort(self):
        # Convert the queue to a list
        queue_list = []
        while not self.is_empty():
            element = self.dequeue()
            queue_list.append(element)

        # Sort the list using built-in sorted() function
        queue_list = sorted(queue_list)

        # Enqueue the sorted elements back into the queue
        for element in queue_list:
            self.enqueue(element)



# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(60)
queue.enqueue(30)
queue.enqueue(70)
queue.enqueue(20)
print("These are the data on the queue")
queue.display()  # Output: 10 60 30 70 20

print("Elements to dequeue are: ")
dequeued_element1 = queue.dequeue()
print("Dequeued element:", dequeued_element1)  # Output: Dequeued element: 10

dequeued_element2 = queue.dequeue()
print("Dequeued element:", dequeued_element2)  # Output: Dequeued element: 60

queue.display()  # Output: 30 70 20




