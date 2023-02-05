def func(data):
    for value in data:
        print('*' * value)


l = list(map(int, input("List: ").split()))
func(l)