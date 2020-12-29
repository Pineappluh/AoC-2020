import fileinput


def solve_expression(expression):
    stack = []
    index = -1

    for char in expression:
        if char.isnumeric():
            stack.append(int(char))
        else:
            stack.append(char)

        index += 1

        while True:
            if index >= 2 and isinstance(stack[index], int) and stack[index - 1] in ['*', '+']:
                operand_2 = stack.pop()
                operator = stack.pop()
                operand_1 = stack.pop()
                stack.append(calculate(operand_1, operator, operand_2))
                index -= 2
            elif stack[index] == ')':
                stack.pop()
                number = stack.pop()
                stack.pop()
                stack.append(number)
                index -= 2
            else:
                break

    return stack[0]


def calculate(operand_1, operator, operand_2):
    if operator == '*':
        return operand_1 * operand_2
    elif operator == '+':
        return operand_1 + operand_2


solution = 0
for line in fileinput.input():
    expression = line.replace(' ', '')
    solution += solve_expression(expression)

print(solution)
