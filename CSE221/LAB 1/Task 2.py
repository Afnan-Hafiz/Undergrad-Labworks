n=int(input())
for i in range (n):
    total=input().split()
    number1=int(total[1])
    number2=int(total[3])
    sign=total[2]
    if sign == '+':
        result = number1 + number2
    elif sign == '-':
        result = number1 - number2
    elif sign == '*':
        result = number1 * number2
    elif sign == '/':
        result = number1 / number2

    print(round(result,6))