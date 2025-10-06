lst = eval("["+input()+"]")
if len(lst) > 4:
    print(lst[2:-2])
elif len(lst) == 4:
    print([])
else:
    print("Not possible")