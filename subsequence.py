def is_subsequence(subseq, seq):
# Solution using Two Pointers

    i, j = 0, 0
    sub_len, seq_len = len(subseq), len(seq)
    while (i < sub_len and j < seq_len):
        if subseq[i] == seq[j]:
            i += 1
        j += 1
        if i == sub_len:
            break
    return i == sub_len

# Solution using Recursion (RE)
#
#    if sub_len == 0:
#        return True
#    if seq_len == 0:
#        return False
#    if subseq[sub_len-1] == seq[seq_len-1]:
#        return is_subsequence(subseq, seq, sub_len-1, seq_len-1)
#    return is_subsequence(subseq, seq, sub_len, seq_len-1)

# Solution using Stack (TL)
#
#    stack = list(subseq)
#    for char in seq:
#        if stack and stack[0] == char:
#            stack.pop(0)
#    return stack == []


def __read_input():
    subseq = input()
    seq = input()
    return subseq, seq


def main():
    subseq, seq = __read_input()
    return is_subsequence(subseq, seq)


if __name__ == '__main__':
    print(main())
