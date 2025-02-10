def countdown(n):
    for i in range(n, -1, -1):
        yield i

if __name__ == "__main__":
    n = int(input("\nEnter a number for countdown: "))
    print("Countdown from {}:".format(n))
    for number in countdown(n):
        print(number, end=" ")
    print()