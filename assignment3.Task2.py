import math

try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and natural log are not defined for negative numbers.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        print(f"Square root of {number} is {square_root}")
        print(f"Natural logarithm (log base e) of {number} is {natural_log}")

    sine_value = math.sin(number)
    print(f"Sine of {number} radians is {sine_value}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
