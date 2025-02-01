def solve(num_heads, num_legs):
    # x = кол-во кур, y = кол-во кроликов

    # x + y = num_heads
    # 2x + 4y = num_legs

    # x = num_heads - y

    # => 2*(num_heads - y) + 4y = num_legs
    # => 2*num_heads - 2y + 4y = num_legs
    # => 2*num_heads + 2y = num_legs
    # => 2y = num_legs - 2*num_heads

    # => y = (num_legs - 2*num_heads) / 2
    y = (num_legs - 2 * num_heads) // 2
    x = num_heads - y

    return x, y

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")