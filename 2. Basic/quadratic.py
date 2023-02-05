# x^2 - 3x - 10

a = 1
b = -3
c = -10

# Your code here
discriminant = ((b ** 2) - 4 * a * c) ** (0.5)
first_solution = (-b + discriminant) / (2 * a)
second_solution = (-b - discriminant) / (2 * a)
# ^^^^^^^^^^^^^^

print("x = " + str(first_solution))
print("x = " + str(second_solution))