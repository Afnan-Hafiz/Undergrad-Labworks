from os import curdir
def task4A_recursive( head ):
    cur = head
    if cur.next == None:
      print(cur.elem,end= " ")
      return
    task4A_recursive( cur.next )
    print(cur.elem,end= " ")

def task4B_recursive( head,prev = None):
    cur = head
    front = cur.next
    if cur.next == None:
      cur.next = prev
      head = cur
      return head
    else:
      cur.next = prev
      prev = cur
      cur = front
      front = front.next
    cur = task4B_recursive( cur,prev )
    return cur

# Driver Code for Task-4
# task4A_recursive
arr = np.random.randint(1, 20, size=6, dtype=int)

print("task4A_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",str(arr[::-1])[1:-1] )
print( "Your Output    : ",end="" )
task4A_recursive( head )
print()

#--------------------------------------------------------

# task4B_recursive
print("\ntask4B_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",str(arr[::-1])[1:-1] )
print( "Your Output    : ",end="" )
head = task4B_recursive( head )
showLL(head)
print()