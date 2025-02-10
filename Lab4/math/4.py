def parallelogram_area():
    base = float(input("\nLength of base: "))
    height = float(input("Height of parallelogram: "))
    area = base * height
    print("Area of parallelogram: {:.1f}".format(area))

if __name__ == "__main__":
    parallelogram_area()