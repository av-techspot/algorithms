def recursive_binary_search(arr, bike_price, right, left):
    if right < left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= bike_price and arr[mid-1] < bike_price:
        return mid
    elif bike_price < arr[mid]:
        return recursive_binary_search(arr, bike_price, mid, left)
    else:
        return recursive_binary_search(arr, bike_price, right, mid + 1)


def __read_input():
    days_amount = int(input())
    days_cash = [0] + list(map(int, input().split()))
    bike_price = int(input())
    return days_amount, days_cash, bike_price


def main():
    day_1 = recursive_binary_search(days_cash, bike_price, right, left=0)
    day_2 = recursive_binary_search(days_cash, bike_price * 2, right, left=0)
    return day_1, day_2


if __name__ == '__main__':
    right, days_cash, bike_price = __read_input()
    print(*main())
