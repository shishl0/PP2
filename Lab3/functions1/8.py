def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if len(code) > 0 and n == code[0]:
            code.pop(0)
    return len(code) == 0


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))