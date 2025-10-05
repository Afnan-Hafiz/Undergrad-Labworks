from types import new_class
def findMax_recursive( head, max = 0, new = 0 ):
    max = head.elem
    if head.next == None:
      return max
    new = findMax_recursive(head.next)
    if max> new:
      return max
    else:
      return new
def findMax_recursive2( head,  new = 0 ):
    if head.next == None:
      return head
    new = findMax_recursive2(head.next)
    if head.elem< new.elem:
      return head
    else:
      return new
def sortLL_recursive( head ):
    if head.next == None:
      return head
    mac_val = findMax_recursive2( head.next)
    if head.elem>=mac_val.elem:
        head.elem,mac_val.elem = mac_val.elem,head.elem
    sortLL_recursive( head.next )
    return head
def finDup(head,cur,i = 0):
  count  = ""
  while head != None:
    if cur.elem == head.elem and cur != head:
      if count!= "":
        count += ", "+str(i)
      else:
        count += str(i)
    head = head.next
    i += 1
  if count != "":
    return count
  else:
    return "No duplicate"

def findDup( head,cur = None, i = -1 ):
    i+=1
    if cur == None:
      cur = head
    if cur.next == None:
      print(f"{cur.elem}"+": "f"{finDup(head,cur,i)}")
      return cur
    print(f"{cur.elem}"+": "f"{finDup(head,cur,i)}")
    findDup( head,cur.next,-1 )
    return head

# Driver Code for Task-5
arr = np.random.randint(1, 20, size=6, dtype=int)

# task5A
print("findMax_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",np.max(arr) )
print( "Your Output    : ",findMax_recursive(head) )

#--------------------------------------------------------

# task5B
print("\nsortLL_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",str(np.sort(arr))[1:-1] )
print( "Your Output    : ",end="" )
head = sortLL_recursive( head )
showLL(head)
print()

#--------------------------------------------------------

# task5C
print("\nfindDup: ")
print("The LinkedList: ",end="")
arr = np.array([10, 22, 13, 20, 22, 23, 10, 22])
head = arr2LL( arr )
showLL(head)
print( "\nExpected Output: " )
print("10: 6\n22: 4, 7\n13: No Duplicate\n20: No Duplicate\n22: 1, 7\n23: No Duplicate\n10: 0\n22: 1, 4\n")
print( "Your Output    : ",end="\n" )
findDup( head )
print()