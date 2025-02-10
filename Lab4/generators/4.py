def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

if __name__ == "__main__":
    a = int(input("\nEnter the starting number (a): "))
    b = int(input("Enter the ending number (b): "))
    print("Squares from {} to {}:".format(a, b))
    for sq in squares(a, b):
        print(sq, end=" ")
    print()