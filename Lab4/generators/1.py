def squares_generator(n):
    for i in range(n + 1):
        yield i ** 2

if __name__ == "__main__":
    N = int(input("What is the N ? :"))
    print("\n=== Squares up to", N, "===")
    for square in squares_generator(N):
        print(square, end=" ")
    print()