# id 87401567

def broken_search(nums, target) -> int:
    length = len(nums)
    return binary_search(nums, 0, length-1, target)


def binary_search(arr, left, right, key):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':

    def test():
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6

    def read_input():
        length = int(input())
        key = int(input())
        arr = list(map(int, input().split()))
        return length, key, arr

    def main():
        _, key, arr = read_input()
        print(broken_search(arr, key))

    main()
