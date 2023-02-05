def divide_by(a, b):
    if b == 0:
        return 0
    return a / b


# For testing
assert divide_by(10, 2) == 5
assert divide_by(90, 5) == 18
assert divide_by(2, 4) == 0.5
assert divide_by(7, 0) == 0