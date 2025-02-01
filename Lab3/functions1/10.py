def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


my_list = [1, 2, 2, 3, 3, 3, 4, 4]
print(unique_list(my_list))