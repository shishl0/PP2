def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]


my_list = [1, 2, 3, 4, 5, 17, 18, 19, 20, 23]
primes = filter_prime(my_list)
print("Prime numbers from the list:", primes)