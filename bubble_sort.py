def bubble_sort(length, arr):
    flag = True
    for i in range(length-1):
        if_flag = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if_flag = True
                flag = False
        if if_flag:
            print(' '.join(list(map(str, arr))))
    if flag:
        print(' '.join(list(map(str, arr))))


def __read_input():
    length = int(input())
    arr = list(map(int, input().split()))
    return length, arr


def main():
    length, arr = __read_input()
    bubble_sort(length, arr)


if __name__ == '__main__':
    main()
