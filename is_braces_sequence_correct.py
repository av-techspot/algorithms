class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
seq = '({]})'


def is_correct_bracket_seq(seq):
    if not seq:
        return True
    for bracket in seq:
        if bracket in '([{':
            stack.push(bracket)
        else:
            if stack.is_empty():
                return False
            left = stack.pop()
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            elif left == '{':
                right = '}'
            if right != bracket:
                return False
    return stack.is_empty()


if __name__ == '__main__':
    print(is_correct_bracket_seq(seq))
