#4
inp1 = input("Enter a string of number separated by a space: ")
while inp1 != "STOP":
  lst1 = inp1.split()
  lst2 = []
  for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
  for i in range(len(lst1)-1):
    sum = lst1[i]-(lst1[i+1])
    if sum < 0:
      sum = sum-sum-sum
    lst2.append(sum)
  for i in range(len(lst2)):
    lst2[i] = int(lst2[i])
  for i in range(len(lst2)-1):
    for j in range(len(lst2)-1):
      if lst2[j] > lst2[j+1]:
        lst2[j],lst2[j+1] = lst2[j+1],lst2[j]
  c = 1
  for i in range(len(lst2)):
    if lst2[i] == c:
      c+=1
      ans = "UB Jumper"
    else:
      flag = False
      ans = "Not UB Jumper"
      break
  print(ans)
  inp1 = input("Enter a string of number separated by a space: ")