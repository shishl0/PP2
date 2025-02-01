def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

f_temp = 100
print(f"{f_temp}F is equal to {fahrenheit_to_celsius(f_temp):.2f}C.")