def arithmetic_arranger(problems, show_answers=True):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists for the arranged rows
    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []  # Optional row for answers

    # Iterate over each problem
    for problem in problems:
        # Check if the operator is valid
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."

        # Split the problem into components
        operand = problem.split(' ')  # e.g., "32 + 698" -> ["32", "+", "698"]
        first_operand = operand[0]   # "32"
        operator = operand[1]        # "+"
        second_operand = operand[2]  # "698"

        # Validate if the operands are digits
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."

        # Validate operand length
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of each row for each problem
        width = max(len(first_operand), len(second_operand)) + 2

        # Format the components for each row into lists
        top_row.append(first_operand.rjust(width)) # top_row = ['  32', '3801']
        bottom_row.append(operator + second_operand.rjust(width - 1)) # bottom_row = ['+ 698', '-    2']
        dash_row.append('-' * width) # dash_row = ['-----', '------']

        # Compute the answer if requested
        if show_answers:
            if operator == '+':
                answer = int(first_operand) + int(second_operand)
            else:
                answer = int(first_operand) - int(second_operand)
            answer_row.append(str(answer).rjust(width))

    # Join each row with four spaces in between
    arranged_top = '    '.join(top_row) # arranged_top = '  32    3801'
    arranged_bottom = '    '.join(bottom_row) # arranged_bottom = '+ 698    -    2'
    arranged_dashes = '    '.join(dash_row) # arranged_dashes = '-----    ------'
    arranged_answers = '    '.join(answer_row) if show_answers else ""

    # Combine rows into the final output, with new lines starting at each index in the given list
    if show_answers:
        arranged_problems = '\n'.join([arranged_top, arranged_bottom, arranged_dashes, arranged_answers])
    else:
        arranged_problems = '\n'.join([arranged_top, arranged_bottom, arranged_dashes])

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')