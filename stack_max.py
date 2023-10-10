class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            return sorted(self.items)[-1]
        return 'None'


def read_input():
    length = int(input())
    commands = []
    for command in range(length):
        commands.append(input())
    return commands


def output():
    stack = StackMax()
    commands = read_input()
    for i in range(len(commands)):
        if commands[i] == 'get_max':
            print(stack.get_max())
        elif commands[i].startswith('push'):
            push_x = commands[i].split()
            stack.push(int(push_x[1]))
        elif commands[i] == 'pop':
            stack.pop()


if __name__ == '__main__':
    output()
