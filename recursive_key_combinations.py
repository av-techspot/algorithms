KEY_VALUES = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def key_combinations(keys, index, combinations, result=''):
    if index == -1:
        combinations.append(result)
        return
    else:
        digit = keys[index]
        length = len(KEY_VALUES[digit])
        for i in range(length):
            key_combinations(
                keys, index - 1, combinations, KEY_VALUES[digit][i] + result
            )


def __read_input():
    return str(input())


def main():
    length = len(keys)
    combinations = list()
    key_combinations(keys, length - 1, combinations)
    combinations.sort()
    return ' '.join(combinations)


if __name__ == '__main__':
    keys = __read_input()
    print(main())
