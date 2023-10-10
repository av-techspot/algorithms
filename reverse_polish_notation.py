# успешное решение 87021501

import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items:
            return self.items.pop()
        raise Exception('Stack is empty')


def calculate(stack):
    for elem in expression:
        if elem not in OPERATORS:
            stack.push(int(elem))
        else:
            right, left = stack.pop(), stack.pop()
            stack.push(OPERATORS[elem](left, right))

    return stack.pop()


if __name__ == '__main__':
    def __read_input():
        return input().split()

    def main():
        stack = Stack()
        return calculate(stack)

    expression = __read_input()
    print(main())
