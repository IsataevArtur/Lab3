def func(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(func([1, 3, 3]))

print(func([1, 3, 1, 3]))

print(func([3, 1, 3]))
