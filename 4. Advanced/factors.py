def get_factors(number):
    # The recursive case is first.
    # If the number is divisible this should run.
    for i in range(2, number):
        if number % i == 0:
            return get_factors(i) + get_factors(number // i)
    
    # This is the base case. Is run when the number is
    # not divisible. Rare to see the base case after the
    # recursive case but it makes sense here.
    return [number]

print(get_factors(2520))