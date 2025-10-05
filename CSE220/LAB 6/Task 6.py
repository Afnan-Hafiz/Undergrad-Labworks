def level_sum(root):
  if root==None:
    return
  else:
    level=findlevel(root)
    output=0
    for i in level.keys():
      if i%2==0:
        output-=level[i]
      else:
        output+=level[i]
  return output


def findlevel(root, level = {}, i = 0):
  if root!=None:
    if i in level.keys():
      level[i]+=root.elem
    else:
      level[i]=root.elem
    i+=1

    findlevel(root.left, level, i)
    findlevel(root.right, level, i)

  return level




#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4