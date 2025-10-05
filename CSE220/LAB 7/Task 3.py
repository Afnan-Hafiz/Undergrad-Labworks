def sum_of_leaves(root, sum):
  if root==None:
    return 0

  if root.left==None and root.right==None:
    sum+=root.elem

  else:
    return sum_of_leaves(root.left, sum) + sum_of_leaves(root.right, sum)


  return sum


tree_array = [None,30,10,40,3,15,35,55,2,None,None,None,None,36,None,None]
root = tree_construction(tree_array)
print(sum_of_leaves(root, 0))