#with append
lst = []
for i in range(5):
    n= int(input())
    lst.append(n)
print(lst)

#without append
lst = []
for i in range(5):
    n = int(input())
    lst = lst + [n]
    print(lst)