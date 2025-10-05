def task2A( arr ):
  idx = 0
  while idx < len(arr):
    print(arr[idx],end = " ")
    idx +=1
  print()

def task2B_recursive( arr,idx = 0,i = 0):
  idx = len(arr)
  i+=1
  idx-=i
  if idx == 0:
    print(arr[idx],end = " ")
    return
  task2B_recursive(arr,idx,i)
  print(arr[idx],end = " ")
def task2C( arr ):
  sum = 0
  for i in arr:
    sum += i
  return sum

def task2D_recursive( arr , idx = -1):
  idx+=1
  if idx == len(arr)-1:
    return arr[idx]
  new = task2D_recursive(arr,idx)
  return new+arr[idx]

def task2E( arr):
  even_sum = 0
  odd_sum = 1
  for i in arr:
    if i%2 == 0:
      even_sum+=i
    else:
      odd_sum*=i
  return float(odd_sum-even_sum)
def task2F_recursive( arr ,idx = -1,new = 0,odd_new =1,sum =0):
  if idx == len(arr)-1:
    return odd_new-new
  idx += 1
  if arr[idx]%2 == 0:
    new+=arr[idx]
    sum = task2F_recursive(arr,idx,new,odd_new)
  else:
    odd_new*=arr[idx]
    sum = task2F_recursive(arr,idx,new,odd_new)
  return sum


# Driver Code for Task-2
# task2A
print("Task2A: ")
arr = np.random.randint(1, 20, size=6, dtype=int)
print( "Expected Output: "+str(arr)[1:-1] )
print( "Your Output    : ",end="" )
task2A( arr )
print()

# task2B_recursive
print("\nTask2B_recursive: ")
print( "Expected Output: ",str(arr)[1:-1] )
print( "Your Output    : ",end="" )
task2B_recursive( arr )
print()

# task2C
print("\nTask2C: ")
arr = np.random.randint(1, 10, size=6, dtype=int)
print("The Array: ",arr)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task2C(arr) )

# task2D_recursive
print("\nTask2D_recursive: ")
print("The Array: ",arr)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task2D_recursive( arr ) )

# task2E
print("\nTask2E: ")
arr = np.random.randint(1, 8, size=5, dtype=int)
print("The Array: ",arr)
print( "Expected Output: ",np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0]) )
print( "Your Output    : ",task2E( arr ) )


# task2F
print("\nTask2F_recursive: ")
print("The Array: ",arr)
print( "Expected Output: ",int(np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0])) )
print( "Your Output    : ",task2F_recursive( arr ))