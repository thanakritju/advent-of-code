

T_LPAREN = "("
T_RPAREN = ")"
T_OPERATIONS = "+*"
T_NUMBER = "0123456789"

Operations = {
    T_OPERATIONS[0]: (lambda a, b: a + b),
    T_OPERATIONS[1]: (lambda a, b: a * b),
}


def calculate(expressions, precedence=False):
    tokens = expressions.replace("(", "( ").replace(")", " )").split(" ")
    output_queue = []
    operator_stacks = []
    while tokens:
        token = tokens.pop(0)
        if is_sym(token, T_NUMBER):
            output_queue.append(token)
        elif is_operator(token):
            while (
                operator_stacks and
                not is_sym(operator_stacks[-1], T_LPAREN) and
                is_greater_precedence(operator_stacks[-1], token, precedence)
            ):
                output_queue.append(operator_stacks.pop())
            operator_stacks.append(token)
        elif is_sym(token, T_LPAREN):
            operator_stacks.append(token)
        elif is_sym(token, T_RPAREN):
            while not is_sym(operator_stacks[-1], T_LPAREN):
                output_queue.append(operator_stacks.pop())
            if is_sym(operator_stacks[-1], T_LPAREN):
                operator_stacks.pop()

    while operator_stacks:
        output_queue.append(operator_stacks.pop())

    stack = []
    for token in output_queue:
        if is_operator(token):
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = Operations[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


def is_greater_precedence(operator_at_top_stacks, operator, feature_flag):
    if not feature_flag:
        return True
    else:
        operator_at_top_stacks_level = T_OPERATIONS.find(
            operator_at_top_stacks)
        operator_level = T_OPERATIONS.find(operator)
        return operator_at_top_stacks_level < operator_level


def is_sym(token, symbol):
    return token in symbol


def is_operator(token):
    return is_sym(token, T_OPERATIONS)
