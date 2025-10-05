sum_list = []
num_list = []
num = int(input("Enter the number of lists:"))
for i in range(num):
  inp = input("Enter a string of number separated by a space:")
  lst1 = inp.split()
  for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
  num_list.append(lst1)
  sum1 = 0
  for i in range(len(lst1)):
    sum1+=lst1[i]
  sum_list.append(sum1)
max1 = 0
index1 = 0
for i in range(len(sum_list)):
  if sum_list[i]>= max1:
    max1 = sum_list[i]
    index1 = i
print(sum_list[index1])
print(num_list[index1])