def func(nums):
    a = [0, 0, 7, 'a']
    for num in nums:
        if num == a[0]:
            a.pop(0)
    return a==['a']

print(func([1,2,4,0,0,7,5]))
print(func([1,0,2,4,0,5,7]))
print(func([1,7,2,0,4,5,0]))