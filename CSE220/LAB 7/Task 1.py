def LCA(root, x, y):
  if root==None:
    return
  if (x<=root.elem and y>=root.elem) or (x>=root.elem and y<=root.elem):
    return root.elem
  elif x<root.elem and y<root.elem:
    return LCA(root.left, x, y)
  else:
    return LCA(root.right, x, y)
  return root.elem


#DRIVER CODE
root = BTNode(15)
n1 = BTNode(10)
n2 = BTNode(25)
n3 = BTNode(8)
n5 = BTNode(12)
n6 = BTNode(6)
n7 = BTNode(9)
n8 = BTNode(20)
n9 = BTNode(30)
n10 = BTNode(18)
n11 = BTNode(22)

root.left = n1
root.right = n2
n1.left = n3
n2.left = n8
n1.right = n5
n2.right = n9
n3.left = n6
n8.left = n10
n8.right = n11
n3.right = n7

a=LCA(root, 6, 12)
b=LCA(root, 20,6)
c=LCA(root, 18,22)
d=LCA(root, 20,25)
e=LCA(root, 10, 12)

print(a)
print(b)
print(c)
print(d)
print(e)

