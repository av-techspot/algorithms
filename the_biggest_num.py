def find_the_biggest_num(length, numbers):
    for i in range(1, length):
        item_to_insert = numbers[i]
        j = i
        while j > 0 and compare_numbers(item_to_insert, numbers[j-1]):
            numbers[j] = numbers[j-1]
            j -= 1
        numbers[j] = item_to_insert
    return int(''.join(numbers))


def compare_numbers(num_1, num_2):
    return num_1 + num_2 > num_2 + num_1


def __read_input():
    length = int(input())
    numbers = input().split()
    return length, numbers


def main():
    length, numbers = __read_input()
    return find_the_biggest_num(length, numbers)


if __name__ == '__main__':
    print(main())
