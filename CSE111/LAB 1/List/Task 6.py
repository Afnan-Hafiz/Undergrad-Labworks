c = 0
inp = input()
lst = inp.split()
lst1 = []
for i in range(int(lst[0])):
  inp1 = int(input("Enter the number of times student have competed:"))
  lst1.append(inp1)
for i in lst1:
  if 5-int(i) >= int(lst[1]):
    c+=1
print(c//3)