import all_of_them
from all_of_them import grams_to_ounces, filter_prime

def main():
    print(grams_to_ounces(100))
    primes = filter_prime([1,2,3,4,5,7,9,13,17])
    print("Primes:", primes)


if __name__ == "__main__":
    main()