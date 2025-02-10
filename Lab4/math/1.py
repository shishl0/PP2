import math

def degree_to_radian():
    degree = float(input("\nInput degree: "))
    radian = math.radians(degree)
    print("Output radian: {:.6f}".format(radian))

if __name__ == "__main__":
    degree_to_radian()