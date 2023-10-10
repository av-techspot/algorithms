def braces_seq_gen(length, left, right, seq):
    if left == length and right == length:
        print(seq)
    else:
        if left < length:
            braces_seq_gen(length, left+1, right, seq+'(')
        if right < left:
            braces_seq_gen(length, left, right+1, seq+')')


def __read_input():
    return int(input())


def main():
    braces_seq_gen(length, 0, 0, '')


if __name__ == '__main__':
    length = __read_input()
    main()
