# Успешное решение: 87019125

class DequeError(Exception):
    pass


class Deque:
    def __init__(self, deque_max):
        self.cells = [None] * deque_max
        self.max_n = deque_max
        self.head = 0
        self.tail = 1
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def push_front(self, value):
        if self.size == self.max_n:
            raise DequeError
        self.cells[self.head] = value
        self.head = (self.head - 1) % self.max_n
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeError
        self.head = (self.head + 1) % self.max_n
        value = self.cells[self.head]
        self.cells[self.head] = None
        self.size -= 1
        return value

    def push_back(self, value):
        if self.size == self.max_n:
            raise DequeError
        self.cells[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise DequeError
        self.tail = (self.tail - 1) % self.max_n
        value = self.cells[self.tail]
        self.cells[self.tail] = None
        self.size -= 1
        return value


def calculate(deque):
    for el in commands:
        command, *value = el.split()
        try:
            call = getattr(deque, command)
            if value:
                call(value)
            else:
                print(*call())
        except DequeError:
            print('error')


if __name__ == '__main__':

    def __read_input():
        commands_num = int(input())
        deque_max = int(input())
        commands = []
        for _ in range(commands_num):
            commands.append(input())
        return deque_max, commands

    def main():
        deque = Deque(deque_max)
        calculate(deque)

    deque_max, commands = __read_input()
    main()
