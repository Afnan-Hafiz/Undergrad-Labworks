def assemble_conga_line(conga_line):
  count=conga_line
  while count!=None and count.next!=None:
    if count.elem > count.next.elem:
      return False
    count=count.next
  return True

#driver
print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print True
unittest.output_test(returned_value, True)
print()
print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,44,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print False
unittest.output_test(returned_value, False)
print()