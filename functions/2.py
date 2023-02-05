def func(far):
    c = 5/9 * (far - 32)
    print(f"Температура в цельсий {c}")
f = int(input("Температура в фаренгейте: "))
func(f)