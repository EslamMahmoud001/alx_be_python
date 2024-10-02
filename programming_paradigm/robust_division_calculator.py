def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        result = num1/num2
    except ValueError:
        return f"Error: Please enter numeric values only."
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    else:
        return f"The result of the division is {result}"