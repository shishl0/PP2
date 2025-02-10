def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

if __name__ == "__main__":
    n = int(input("\nEnter a number for divisible by 3 and 4 generator: "))
    print("Numbers divisible by 3 and 4 between 0 and {}:".format(n))
    for number in divisible_by_3_and_4(n):
        print(number, end=" ")
    print()