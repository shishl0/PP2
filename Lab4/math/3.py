import math

def regular_polygon_area():
    num_sides = int(input("\nInput number of sides: "))
    side_length = float(input("Input the length of a side: "))
    if num_sides < 3:
        print("A polygon must have at least 3 sides.")
        return
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
    print("The area of the polygon is: {:.2f}".format(area))

if __name__ == "__main__":
    regular_polygon_area()