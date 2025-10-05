def avm(one):
  lis=[]
  x=one.split(" ")
  total=0
  for i in x:
    lis.append(int(i))
  for i in lis:
    total+=i
  average= round(total/len(lis),1)
  return average
one=input()
print(avm(one))