def all_true(t):
    return all(t)

n = tuple(input("Enter the tuple: ").split(" ")) # All elements got by string
print(all_true(n))