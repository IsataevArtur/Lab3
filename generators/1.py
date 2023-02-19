n = int(input())
a = (i**2 for i in range(1,10000000000000000000000000000000))
for i in a:
    if i <= n:
        print(i)
    else:
        break

