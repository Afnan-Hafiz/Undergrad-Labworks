def smallest_level(root, level = {}, i = 0):
  if root==None:
    return

  else:
    if i in level.keys():
      if root.elem<level[i]:
        level[i]=root.elem
    else:
      level[i]=root.elem
    i+=1

  smallest_level(root.left,level,i)
  smallest_level(root.right,level,i)
  return level


#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}