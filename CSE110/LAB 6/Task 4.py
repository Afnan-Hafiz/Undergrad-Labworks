list_one = eval(input())
list_two = eval(input())
flag = False
for i in list_one:
    if i in list_two:
        flag = True
        break
print(flag)