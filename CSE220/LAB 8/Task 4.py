#TASK 4
def maxExt(self,k):
  maxheap=MaxHeap(len(self))
  s=np.array([None]*k)
  size=len(self)

  for i in range(size):
    maxheap.insert(self[i])

  for i in range(len(s)):
    a=maxheap.extractMax()
    s[i]=a

  return s

#DRIVER CODE
nums = [4, 10, 2, 8, 6, 7]
k = 3
print(maxExt(nums,k))