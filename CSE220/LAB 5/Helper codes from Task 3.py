class Node:
  def __init__(self, value=None, next = None):
    self.elem = value
    self.next = next
    
def showLL(head):
  if head!=None:
    n = head
    while n!=None:
        print(n.elem, end=' -> ')
        n = n.next
    print()

def arr2LL(arr):
  head = Node(arr[0])
  n = head
  for i in range(1,len(arr)):
      newNode = Node(arr[i])
      n.next = newNode
      n = newNode
  tail = n
  return head