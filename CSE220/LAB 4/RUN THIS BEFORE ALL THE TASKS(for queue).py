# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        

# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, elem):
        new_node = Node(elem)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        removed_elem = self.front.elem
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_elem

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.front.elem

    def is_empty(self):
        return self.front is None

    def display_queue(self):
        print("Queue (front to rear):", end=" ")
        current = self.front
        while current:
            print(f"{current.elem} ->", end=" ")
            current = current.next
        print("NULL")