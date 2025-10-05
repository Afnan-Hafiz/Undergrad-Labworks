def average_mark(*args):
  count=0
  total=0
  for i in args:
    count+=1
  for i in args:
    total+=i
  average= round(total/count,1)
  return average
a=average_mark(3,4,5,3)
print(a)