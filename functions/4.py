def func(numbers):
    primetest = lambda num: num > 1 and all(num % i != 0 for i in range(2, num))

    return list(filter(primetest, numbers))

inp = input("Numbers: ")
numbers = list(map(int, inp.split()))
prime_numbers = func(numbers)

print("Prime numbers:", prime_numbers)