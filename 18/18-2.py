import fileinput


def solve_expression(expression_stack):
    if len(expression_stack) == 1:
        return expression_stack[0]

    level = 0
    addition_state = [False]

    for x in expression_stack:
        if x == '+':
            addition_state[level] = True
        elif x == '(':
            addition_state.append(False)
            level += 1
        elif x == ')':
            level -= 1

    level = 0
    stack = []
    index = -1
    for x in expression_stack:
        stack.append(x)

        if x == '(':
            level += 1
        elif x == ')':
            level -= 1

        index += 1

        while True:
            if index >= 2 and isinstance(stack[index], int) and isinstance(stack[index - 2], int) and \
                    (stack[index - 1] == '+' or stack[index - 1] == '*' and not addition_state[level]):
                operand_2 = stack.pop()
                operator = stack.pop()
                operand_1 = stack.pop()
                stack.append(calculate(operand_1, operator, operand_2))
                index -= 2
            elif stack[index] == ')' and stack[index - 2] == '(':
                stack.pop()
                number = stack.pop()
                stack.pop()
                stack.append(number)
                index -= 2
            else:
                break

    return solve_expression(stack)


def create_stack(expression):
    stack = []
    for char in expression:
        if char.isnumeric():
            stack.append(int(char))
        else:
            stack.append(char)

    return stack


def calculate(operand_1, operator, operand_2):
    if operator == '*':
        return operand_1 * operand_2
    elif operator == '+':
        return operand_1 + operand_2


solution = 0
for line in fileinput.input():
    expression = line.strip().replace(' ', '')
    solution += solve_expression(create_stack(expression))

print(solution)
