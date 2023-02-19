import math
a = int(input())
b = int(input())
h = int(input())
Y = int(input())
if Y == 90:
    S = a * h
    print("Area of parallelogram",S)
else:
    S = a * b * math.sin(Y)
    print("Area of parallelogram",S)
    