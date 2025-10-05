def task3A( head ):
  while head!= None:
    print(head.elem,end = " ")
    head = head.next


def task3B_recursive( head ):
    if head.next  == None:
      return
    print(head.elem,end = " ")
    task3B_recursive( head.next )

def task3C( head ):
    sum = 0
    while head != None:
      sum+= head.elem
      head = head.next
    return sum

def task3D_recursive( head):
    if head.next == None:
      return head.elem
    new = task3D_recursive( head.next)
    return new+head.elem

def task3E( head ):
    new = 1
    odd_new = 0
    while head != None:
      if head.elem %2 == 0:
        new *= head.elem
      else:
        odd_new += head.elem
      head = head.next
    return odd_new-new

def task3F_recursive( head,new=1,odd_new=0 ):
    if head == None:
      return odd_new-new
    if head.elem%2 == 0:
      new*=head.elem
      head = head.next
      sum = task3F_recursive(head,new,odd_new)
    else:
      odd_new+=head.elem
      head = head.next
      sum = task3F_recursive(head,new,odd_new)
    return sum


# Driver Code for Task-3
arr = np.random.randint(1, 20, size=6, dtype=int)

# task3A
print("task3A: ")
print( "Expected Output: "+str(arr)[1:-1] )
print( "Your Output    : ",end="" )
head = arr2LL(arr)
task3A( head )
print()

# task3B_recursive
print("\ntask3B_recursive: ")
print( "Expected Output: ",str(arr)[1:-1] )
print( "Your Output    : ",end="" )
head = arr2LL(arr)
task3B_recursive( head )
print()

#--------------------------------------------------------

arr = np.random.randint(1, 10, size=6, dtype=int)

# task3C
print("\ntask3C: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task3C( head ) )

# task3D_recursive
print("\ntask3D_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task3D_recursive( head ) )

#--------------------------------------------------------

arr = np.random.randint(1, 8, size=5, dtype=int)

# task3E
print("\ntask3E: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",np.sum([e for e in arr if e%2!=0])-np.prod([e for e in arr if e%2==0]) )
print( "Your Output    : ",task3E( head ) )

#--------------------------------------------------------

# task3F
print("\ntask3F_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",np.sum([e for e in arr if e%2!=0])-np.prod([e for e in arr if e%2==0]) )
print( "Your Output    : ",task3F_recursive( head ) )