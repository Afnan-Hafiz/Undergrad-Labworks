class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None
    
def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)
  
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)