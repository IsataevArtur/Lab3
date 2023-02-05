def func(radius):
    return 4/3 * 3.14 * (radius ** 3)
radius = int(input("R: "))
volume = func(radius)
print("V: %.2f" % volume)