inp1 = input("Enter a string of number separated by a space:")
lst1 = inp1.split()
inp2 = input("Enter a string of number separated by a space:")
lst2 = inp2.split()
lst3 = []
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
for i in range(len(lst2)):
    lst2[i] = int(lst2[i])
for i in lst1:
  for j in lst2:
    lst3.append(i*j)
print(lst3)
