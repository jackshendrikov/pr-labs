from math import sin, pow

while True:
    try:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
    except ValueError:
        print("Enter number!")
    else:
        part1 = pow(sin(x + 0.4), 2)
        part2 = pow(y, 2) + 7.325 * x
        try:
            result = part1 / part2
        except ZeroDivisionError:
            print("You cannot divide by zero!")
        else:
            print("F ≈ ", round(result, 6))
            break