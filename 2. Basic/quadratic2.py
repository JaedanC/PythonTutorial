def solve_quadratic(a, b, c):
    # Your code here
    discriminant = ((b ** 2) - 4 * a * c) ** (0.5)
    first_solution = (-b + discriminant) / (2 * a)
    second_solution = (-b - discriminant) / (2 * a)
    return [first_solution, second_solution]


print(solve_quadratic(1, -3, -10))
print(solve_quadratic(4, -8, 4))
print(solve_quadratic(5, -6, 1))
print(solve_quadratic(1, -4, 6.25))