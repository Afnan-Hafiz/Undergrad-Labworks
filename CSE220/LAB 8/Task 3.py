#TASK 3
def loads(self,m):
  min=MinHeap(m)
  size=len(self)

  for i in range(size):
    if i>=m:
      a=min.extractMin()
      b=a+self[i]
      min.insert(b)
    else:
      min.insert(self[i])

  return min.getheap()


#DRIVER CODE
tasks = [2, 4, 7, 1, 6]
m = 4
print(loads(tasks,m))