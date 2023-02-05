def func(list):
    a = []
    for elem in list:
        if not elem in a:
            a.append(elem)
    return a

input_list = [100, 100, 100, 1, 1, 9,10]
print(func(input_list))