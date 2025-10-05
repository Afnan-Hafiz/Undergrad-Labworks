def mirror_sum(root):
  if root==None:
    return 0
  sum=0

  if root.left!=None and root.right!=None:
    if root.left.left!=None and root.right.right!=None:
      sum+=root.left.left.elem+root.right.right.elem
    if root.left.right!=None and root.right.left!=None:
      sum+=mirror_sum(root.left.right)+mirror_sum(root.right.left)
  else:
    return root.elem
  sum+=root.left.elem+root.right.elem

  return sum



#DRIVER CODE

print("---------------------Test#1---------------------")
#Example Tree 1
root = BTNode(10)
n1 = BTNode(6)
n2 = BTNode(15)
n3 = BTNode(3)
n4 = BTNode(8)
n5 = BTNode(12)
n6 = BTNode(20)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n2.left = n5
n2.right = n6
print("Expected Output: 64")
print("You output     :",mirror_sum(root))

print("---------------------Test#2---------------------")

#Example Tree 1
root = BTNode(20)
n1 = BTNode(15)
n2 = BTNode(25)
n3 = BTNode(10)
n4 = BTNode(18)
n5 = BTNode(5)
n6 = BTNode(30)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n3.left = n5
n2.right = n6
print("Expected Output: 80")
print("You output     :",mirror_sum(root))