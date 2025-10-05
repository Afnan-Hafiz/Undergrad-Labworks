class Node:
  def __init__(self, value=None, next = None):
    self.value = value
    self.next = next

class HashTable:
  def __init__(self, length):
    n = Node()
    self.ht = [n] * length
    self.length = length

  def show(self):
    count = 0
    for i in self.ht:
      temp = i
      print(count, end=" ")
      while temp!=None:
        print (temp.value, end="-->")
        temp = temp.next
      count += 1
      print()


#DIY

  def __hash_function(self, key):
    sum=0
    if len(key)%2==0:
      count=0
      for i in range(0,len(key),2):
        a= ord(key[i])
        count+=a
      mod=count % self.length
      sum+=mod
    else:
      count=0
      for i in range(1,len(key),2):
        a= ord(key[i])
        count+=a
      mod=count % self.length
      sum+=mod

    return sum


  def insert(self, key, value):
    newNode=Node((key,value))
    idx= self.__hash_function(key)
    current=self.ht[idx]
    prev=None


    if current.value==None:
      current=newNode
      self.ht[idx]=current
    else:
      while current!=None:
        if current.value[0]==newNode.value[0]:
          current.value=newNode.value
          return
        current=current.next
      current=self.ht[idx]

      if current.value[1]<newNode.value[1]:
        newNode.next=current
        self.ht[idx]=newNode
      else:
        while current!=None:
          if current.value[1]>newNode.value[1] and current.next==None:
            prev=current
            current.next=newNode
            break
          elif current.value[1]>newNode.value[1]:
            prev=current
            current=current.next
          else:
            prev.next=newNode
            newNode.next=current
            break







#Driver Code
ht = HashTable(3)


ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()
print("------------")
ht.insert("apple", 100)
ht.insert("guava", 10)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 100)-->('guava', 10) -->
# 2 ('cherry', 50)-->