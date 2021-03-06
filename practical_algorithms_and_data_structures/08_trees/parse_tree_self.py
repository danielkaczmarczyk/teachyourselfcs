import operator

def build_tree(expression):
    OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }

    LEFT_PAREN = '('
    RIGHT_PAREN = ')'

    tree = {}
    stack = [tree]
    current_node = tree


    for token in expression:
        if token == LEFT_PAREN:
            new_node = {}
            current_node['left'] = new_node
            stack.append(new_node)
            current_node = stack[-1]
        elif token == RIGHT_PAREN:
            current_node = stack.pop()
        elif token in OPERATORS:
            current_node['val'] = token
            new_node = {}
            current_node['right'] = new_node
            stack.append(new_node)
            current_node = stack[-1]
        elif isinstance(int(token), int):
            current_node['val'] = token
            stack.pop()
            current_node = stack[-1]

    return tree

def evaluate(tree):

    OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }

    item = tree['val']
    if isinstance(item, int):
        return item
    else:
        operation = OPERATORS[item]
        return operation(evaluate(tree['left']), evaluate(tree['right']))



if __name__ == "__main__":
    expression = ['(', 3, '+', '(', 4, '*', 5 ,')',')']
    #expression = ['(', 2, '+', 2, ')']
    tree = build_tree(expression)
    print(tree)
    result = evaluate(tree)
    print(result)
