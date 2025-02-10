def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":
    n = int(input("\nEnter a number for even numbers generator: "))
    evens = list(even_numbers_generator(n))
    print("Even numbers between 0 and {}:".format(n))
    print(", ".join(map(str, evens)))