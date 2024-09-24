def perform_operation(num1, num2, operation):
    """ A function that performs basic arithmetic operations. """
    if operation == "add" or operation == "+":
        result = num1 + num2
    elif operation == "subtract" or operation == "-":
        result = num1 - num2
    elif operation == "multiply" or operation == "*":
        result = num1 * num2
    elif operation == "divide" or operation == "/":
        if num2 == 0:
            result = "Cannot Divide By Zero."
        else:
            result = num1 / num2
    else:
        result == 'Inappropriate Operation'
    return result