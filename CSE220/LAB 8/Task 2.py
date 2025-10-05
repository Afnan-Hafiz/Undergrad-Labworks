#TASK 2
import numpy as np

class MaxHeap():
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
        return (idx-1) // 2


    def extractMax(self):
      if self.__size == 0:
        return "Empty Heap"

      max_value = self.__heap[0]
      self.__heap[0]=self.__heap[self.__size-1]
      self.__heap[self.__size-1]= None
      self.__size -= 1
      self.sink(0)
      return max_value

    def sink(self,idx):
      left= self.get_left_child_index(idx)
      right=self.get_right_child_index(idx)
      large=idx


      if left<self.__size and self.__heap[large]<self.__heap[left]:
        large=left

      if right<self.__size and self.__heap[large]<self.__heap[right]:
        large=right

      if large==idx:
        return

      if large!=idx:
        temp=self.__heap[idx]
        self.__heap[idx]=self.__heap[large]
        self.__heap[large]=temp
        self.sink(large)

    def sort(self):
      b = self.__size
      value = b-1

      while self.__size>0:
        self.__heap[value] = self.extractMax()
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

      if parent!=None and self.__heap[idx] > self.__heap[parent]:
        temp=self.__heap[idx]
        self.__heap[idx]=self.__heap[parent]
        self.__heap[parent]=temp
        self.swim(parent)

    def getheap(self):
      return self.__heap

#DRIVER CODE
arr2= [5,1,2,7,10,11,20]
max=MaxHeap(10)

for i in arr1:
  max.insert(i)

print(max.getheap())
max.insert(8)
print(max.getheap())
max.insert(9)
print(f"Full Array: {max.getheap()}")
print(f"Extracted: {max.extractMax()}")
print(max.getheap())
max.sort()
print()
print(f"Final array after sorting:{max.getheap()}")

#final array BST
#       11
#      /  \
#    9     10
#   / \   / \
#  8   5 2   7
# /
# 1