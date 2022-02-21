def solve(input_equation):
    """Solves an equation passed as a string"""

    # Defining constants
    ALL_OPERATORS = ["/", "*", "+", "-"]  # List of valid operators
    NEGATIVE_OPERATOR = "-"  # '-' operator
    EMPTY_STRING = ""  # Empty string

    # Join all consecutive numbers
    equation = []
    temp = EMPTY_STRING

    for char in input_equation:
        if char.isnumeric():
            temp += char

        else:
            if temp != EMPTY_STRING:
                equation.append(temp)

            equation.append(char)
            temp = EMPTY_STRING

    equation.append(temp)

    # If first element is a negative operator, join to the next element (number)
    if equation[0] == NEGATIVE_OPERATOR:
        equation[1] = f"{NEGATIVE_OPERATOR}{equation[1]}"
        equation.pop(0)

    # Perform all operations (following the operators order - PEDMAS)
    for i in range(0, 3, 2):
        operators = ALL_OPERATORS.copy()[i : i + 2]

        while operators[0] in equation or operators[1] in equation:
            for j, _ in enumerate(equation):

                if equation[j] in operators:

                    operator = equation[j]

                    result = eval(f"{equation[j - 1]}{operator}{equation[j + 1]}")

                    if result != int(result):
                        return None

                    equation[j - 1] = int(result)

                    for _ in range(2):
                        equation.pop(j)

                    break

    # Convert equation to string
    result = equation[0]

    # Check if equation is equal to solution
    if input_equation == str(result):
        result = None

    return result
