def sumTree(root):
  if root==None:
    return
  else:
    sum=0
    level=findlevel(root)
    for i in level.keys():
      if i==0:
        sum+=level[i]
      else:
        sum+=level[i]%i

  return sum

def findlevel(root, level = {}, i = 0):
  if root!=None:
    if i in level.keys():
      level[i]+=root.elem%i
    else:
      level[i]=root.elem
    i+=1

    findlevel(root.left, level, i)
    findlevel(root.right, level, i)

  return level



#Driver Code
#Input 1
root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15