def func(numheads, numlegs):
    cntrab = int((numlegs - 2 * numheads)/2)
    cntchick = int(numheads - cntrab)
    print(f"Количество зайцев {cntrab}, количество куриц {cntchick}")
a = int(input("Kоличество голов: "))
b = int(input("Kоличество ног: "))
func(a, b)