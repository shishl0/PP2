from itertools import permutations

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]

def print_permutations(s):
    perm_set = set(permutations(s))
    for perm in perm_set:
        print(''.join(perm))

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False