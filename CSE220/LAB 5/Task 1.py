def task1A():
  i = 1
  while i<=10:
    print(i)
    i+=1

def task1B_recursive(num = 10):
  if num == 1:
    print(num)
    return
  task1B_recursive(num-1)
  print(num)

def task1C(n):
  i = 1
  while i <= n:
    print(i)
    i+=1

def task1D_recursive(num):
  if num == 1:
    print(num)
    return
  task1B_recursive(num-1)
  print(num)


# Driver Code for Task-1
task1A()
task1B_recursive()
task1C(20)
task1D_recursive(14)