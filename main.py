def calculator(num1, num2, operation):
    """Performs basic math operations"""
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero"
    elif operation == '**':
        result = num1 * num2
    else:
        return "Error: Invalid operation"
    
    return f"{num1} {operation} {num2} = {result}"

# Run calculations
if __name__ == "__main__":
    print(calculator(10, 5, '+'))
    print(calculator(10, 5, '-'))
    print(calculator(10, 5, '*'))
    print(calculator(10, 5, '/'))
    print(calculator(2, 3, '**'))
