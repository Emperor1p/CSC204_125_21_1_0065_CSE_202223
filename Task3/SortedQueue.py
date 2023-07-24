from queue import Queue


# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(60)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("These are the data on the queue before sorting:")
queue.display()

# Sort the queue
queue.sort()

print("These are the data on the queue after sorting:")
queue.display()

