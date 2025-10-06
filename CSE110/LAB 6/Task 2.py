lst = eval(input())
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print(rev)