def word_Decoder(head):
  dh=Node(None)
  count=countNode(head)
  r=13%count
  idx=0
  temp=head
  current=dh

  if head==None:
    return None

  while temp!=None:
    if idx>0 and idx%r==0:
      newNode = Node(temp.elem)
      newNode.next = current.next
      current.next = newNode
    idx+=1
    temp=temp.next


  return current


def countNode(head):
    if head == None:
        return 0

    current_node = head
    count = 0
    while current_node != None:
        current_node = current_node.next
        count += 1
    return count


#Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N