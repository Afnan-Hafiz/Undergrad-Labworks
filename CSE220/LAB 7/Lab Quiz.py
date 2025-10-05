def find_path(root, key):
  path = 0
  def helper(root, key, path):
    if root is None:
      return "Path not found"
    path += root.elem
    if root.elem == key:
      return path

    if key < root.elem:
      return helper(root.left, key, path)
    if key > root.elem:
      return helper(root.right, key, path)
  return helper(root, key, path)

  #DRIVER CODE
root=BTNode(30)
n1 = BTNode(10)
n2 = BTNode(3)
n3 = BTNode(15)
n5 = BTNode(40)
n6 = BTNode(35)
n7 = BTNode(55)

root.left = n1
root.right = n5
n1.left = n2
n5.left = n6
n1.right = n3
n5.right = n7

print(find_path(root,15))
#This should print [30,10,15]

print(find_path(root,50))
#This should print No Path Found