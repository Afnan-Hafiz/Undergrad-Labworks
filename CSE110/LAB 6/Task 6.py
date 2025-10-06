list1 = eval(input())
list2 = eval(input())
new_list = []
for i in list1 + list2:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)