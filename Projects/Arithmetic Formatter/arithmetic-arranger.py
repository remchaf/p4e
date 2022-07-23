import re


def arithmetic_arranger(problems, answer=False):
    if type(problems) != list:
        return 'Wrong input : should be a list of strings'
    elif len(problems) > 5:
        return 'Error: Too many problems.'

    arranged_problems = list()

    for operation in problems:
        if len(operation.split(' ')) != 3:
            return 'Wrong input 2'

        [n1, op, n2] = operation.split(' ')

        if re.search('[^\+\-]', op):
            return "Error: Operator must be '+' or '-'."
        elif re.search('[^0-9]', n1) or re.search('[^0-9]', n2):
            return 'Error: Numbers must only contain digits.'
        elif len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(n1), len(n2))
        arranged_operation = [' ' * (length - len(n1) + 2) +
                              n1, op + ' ' * (length - len(n2) + 1) + n2, '-' * (length + 2)]

        if answer:
            result = None
            if op == '+':
                result = int(n1) + int(n2)
            else:
                result = int(n1) - int(n2)
            result = str(result)
            arranged_operation.append(
                ' ' * (length - len(result) + 2) + result)

        if not len(arranged_problems):
            arranged_problems.extend(arranged_operation)
            continue

        for i in range(len(arranged_problems)):
            arranged_problems[i] += '    ' + arranged_operation[i]
    string = ''
    for i in arranged_problems :
        string += i
        if i != arranged_problems[-1] :
            string += '\n'

    return string


print(arithmetic_arranger(
    ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
