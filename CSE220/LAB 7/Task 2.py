def find_path(root, key):
  if root==None:
    return "No Path Found"

  result=getListed(root,key)
  if result=="No Path Found":
    return result
  else:
    return f"Path: {result}"


def getListed(root,key,a=[]):
  if root==None:
    return "No Path Found"
  a.append(root.elem)

  if root.elem==key:
    return a

  if root.elem>key:
    a=getListed(root.left,key,a)

  else:
    a=getListed(root.right,key,a)

  return a



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