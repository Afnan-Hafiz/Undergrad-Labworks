def nested_to_linear(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result += nested_to_linear(i)
        else:
            result.append(i)
    return result

print(nested_to_linear(eval(input())))