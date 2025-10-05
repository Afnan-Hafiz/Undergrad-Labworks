def check_similar(building_1, building_2):
  count1=countNode(building_1)
  count2=countNode(building_2)

  if count1!=count2:
    return "Not Similar"

  while building_1!=None and building_2!=None:
    if building_1.elem!=building_2.elem:
        return "Not Similar"
    building_1=building_1.next
    building_2=building_2.next
  return "Similar"

def countNode(head):
    if head==None:
        return 0

    current_node=head
    count=0
    while current_node!=None:
        current_node=current_node.next
        count+=1
    return count


#driver
print('==============Test Case 1=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Similar'
unittest.output_test(returned_value, 'Similar')
print()

print('==============Test Case 2=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 3=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 4=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()