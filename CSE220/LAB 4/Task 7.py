class CallQueue:
    def __init__(self):
        self.vip_queue = LinkedListQueue()
        self.regular_queue = LinkedListQueue()

    def enqueue_call(self, customer_id, is_vip):
      if is_vip==True:
        self.vip_queue.enqueue(customer_id)
        print(f"Customer {customer_id} added to VIP queue.")
      else:
        self.regular_queue.enqueue(customer_id)
        print(f"Customer {customer_id} added to Regular queue.")

    def dequeue_call(self):
      if not self.vip_queue.is_empty():
        id=self.vip_queue.dequeue()
        print(f"Processing VIP Customer {id}.")
      elif not self.regular_queue.is_empty():
        id=self.regular_queue.dequeue()
        print(f"Processing Regular Customer {id}.")
      else:
        print("No calls in the queue.")

    def display_queue(self):
        print("VIP queue:")
        self.vip_queue.display_queue()
        print("Regular queue:")
        self.regular_queue.display_queue()



# YOU MUST RUN THIS CELL TO TEST YOUR CODE
# If you modify the method calls the outputs will be changed as well
call_center = CallQueue()
# Enqueueing customers
call_center.enqueue_call(101, False)  # Regular customer
call_center.enqueue_call(201, True)   # VIP customer
call_center.enqueue_call(102, False)  # Regular customer
call_center.enqueue_call(202, True)   # VIP customer
call_center.enqueue_call(103, False)  # Regular customer

call_center.display_queue()

# Processing calls
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()  # No more calls

call_center.display_queue()

#   ::Expected Ouput::

# Customer 101 added to Regular queue.
# Customer 201 added to VIP queue.
# Customer 102 added to Regular queue.
# Customer 202 added to VIP queue.
# Customer 103 added to Regular queue.

# VIP Queue:
# Queue (front to rear): 201 -> 202 -> NULL
# Regular Queue:
# Queue (front to rear): 101 -> 102 -> 103 -> NULL

# Processing VIP Customer 201.
# Processing VIP Customer 202.
# Processing Regular Customer 101.
# Processing Regular Customer 102.
# Processing Regular Customer 103.
# No calls in the queue.

# VIP Queue:
# Queue (front to rear): NULL
# Regular Queue:
# Queue (front to rear): NULL