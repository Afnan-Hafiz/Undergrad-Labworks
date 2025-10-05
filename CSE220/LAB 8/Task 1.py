#TASK 1
import numpy as np

class MinHeap():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__heap = np.array([None]*capacity)
        self.__size = 0

    def get_left_child_index(self, idx):
        return 2 * idx + 1

    def get_right_child_index(self, idx):
        return 2 * idx + 2

    def get_parent_index(self, idx):
        if idx == 0:
            return None
        return (idx - 1)//2


    def extractMin(self):
      if self.__size == 0:
        return "Empty Heap"

      min_value = self.__heap[0]
      self.__heap[0]=self.__heap[self.__size-1]
      self.__heap[self.__size-1]=None
      self.__size -= 1
      self.sink(0)
      return min_value

    def sink(self,idx):
      left= self.get_left_child_index(idx)
      right=self.get_right_child_index(idx)
      small=idx


      if left<self.__size and self.__heap[small]>self.__heap[left]:
        small=left

      if right<self.__size and self.__heap[small]>self.__heap[right]:
        small=right

      if small==idx:
        return

      if small!=idx:
        temp=self.__heap[idx]
        self.__heap[idx]=self.__heap[small]
        self.__heap[small]=temp
        self.sink(small)

    def sort(self):
      b = self.__size
      value = b-1

      while self.__size>0:
        self.__heap[value] = self.extractMin()
        value-=1
      self.__size=b

      for i in range(b//2):
        self.__heap[i],self.__heap[(b - 1)-i]=self.__heap[(b - 1)-i],self.__heap[i]

      return self.__heap[b]

    def insert(self, key):
      if self.__size >= self.__capacity:
        print("No Space Left:", key)
        return
      self.__heap[self.__size] = key
      self.swim(self.__size)
      self.__size += 1

    def swim(self,idx):
      parent=self.get_parent_index(idx)
      if idx==0:
        return

      if parent!=None and self.__heap[idx] <= self.__heap[parent]:
        temp=self.__heap[idx]
        self.__heap[idx]=self.__heap[parent]
        self.__heap[parent]=temp
        self.swim(parent)

    def getheap(self):
      return self.__heap

#DRIVER CODE
arr1= [5,1,2,7,10,11,20]
min=MinHeap(10)

for i in arr1:
  min.insert(i)

print(min.getheap())
min.insert(8)
print(min.getheap())
min.insert(9)
print(f"Full Array: {min.getheap()}")
print(f"Extracted: {min.extractMin()}")
print(min.getheap())
min.sort()
print()
print(f"Final array after sorting:{min.getheap()}")


#final array BST
#        2
#      /  \
#    5     9
#   / \   / \
#  7   10 11  20
# /
# 8