def trapezoid_area():
    height = float(input("\nHeight: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    area = height * (base1 + base2) / 2
    print("Area of the trapezoid:", area)

if __name__ == "__main__":
    trapezoid_area()