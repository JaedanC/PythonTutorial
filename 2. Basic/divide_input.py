while True:
    try:
        first = float(input("First number: "))
        break
    except ValueError:
        print("Not a number, try again.")

while True:
    try:
        second = float(input("Second number: "))
        break
    except ValueError:
        print("Not a number, try again.")

try:
    print(first / second)
except ZeroDivisionError:
    print("Division by 0")