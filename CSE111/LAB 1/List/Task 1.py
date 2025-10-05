user = input()
lst1 = []
lst2 = []
lst3 = []
c = 0
while user != "STOP":
  lst1.append(user)
  user = input()
for i in lst1:
  if i not in lst2:
    lst2.append(i)
for i in lst2:
  for j in lst1:
    if i == j:
        c+=1
  lst3.append(c)
  c = 0
for i in lst3:
  print(lst2[c],"-",i,"times")
  c+=1