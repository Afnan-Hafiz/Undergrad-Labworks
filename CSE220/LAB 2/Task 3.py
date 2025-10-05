def idGenerator(head1, head2, head3):
  reversedLL=reverse_out_of_place(head1)
  temp=reversedLL
  temp2=head2
  temp3=head3
  dh=Node(None)
  current=dh

  if head1==None and head2==None and head3==None:
    return None

  for i in range(4):
    if temp!=None:
      current=appendLL(current,temp.elem)
      temp=temp.next


  for i in range(4):
    if temp2!=None and temp3!=None:
      sum=temp2.elem+temp3.elem
      if 10<=sum:
        sum=sum%10
      current=appendLL(current,sum)
      temp2=temp2.next
      temp3=temp3.next

  return current.next



def reverse_out_of_place(head):
    if head == None:
        return None
    rev_head = Node(head.elem)
    temp = head.next
    while temp != None:
        newNode = Node(temp.elem)
        newNode.next = rev_head
        rev_head = newNode
        temp = temp.next
    return rev_head

def get_tail(head):
    temp = head
    while temp.next!=None:
        temp = temp.next
    return temp

def appendLL(head, data):
    newNode = Node(data)
    if head == None:
        head = newNode
        return
    tail = get_tail(head)
    tail.next = newNode
    return head

#driver
print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5