# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None
  
  
  # YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
def print_stack(st):
  if st.isEmpty():
    return
  p = st.pop()
  print('|',p,end=' ')
  if p<10:
    print(' |')
  else:
    print('|')
  #print('------')
  print_stack(st)
  st.push(p)

# st = Stack()
# st.push(4)
# st.push(3)
# st.push(5)
# st.push(1)
# st.push(9)
# print_stack(st)
# print('------')