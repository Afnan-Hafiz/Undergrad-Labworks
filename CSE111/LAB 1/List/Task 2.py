c = int(input("Enter the number of lists:"))
sum = 0
max = 0
lst = []
for i in range(c):
  user = input("Enter a string of number separated by a space:")
  lst1 = user.split()
  for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
  for i in lst1:
    sum += i
  if sum>=max:
    max = sum
    lst = lst1
  sum = 0
print(max)
print(lst)




