def subtract_summation(root):
  if root==None:
    return
  else:
    diff=0
    diff=leftsummation(root.left)-rightsummation(root.right)
  return diff

def leftsummation(root):
  if root==None:
    return 0
  else:
   return root.elem + leftsummation(root.left) + leftsummation(root.right)

def rightsummation(root):
  if root==None:
    return 0
  else:
   return root.elem + rightsummation(root.left) + rightsummation(root.right)


#Driver Code
root=BTNode(71)
tree_array = [None, 71, 27, 62, 80, 75, 41, 3, 87, 56, None, None, None, None, 19, 89]
root = tree_construction(tree_array)
print(subtract_summation(root)) #This should print 111