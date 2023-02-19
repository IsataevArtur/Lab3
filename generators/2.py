n =int(input())
l = []
a = (i for i in range(1, n + 1))
for i in a:
    if i % 2 == 0:
        l.append(i)
print(*l, sep = ', ')