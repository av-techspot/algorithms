def find_finished_flowerbeds(length, arr):
    sorted_arr = sorted(arr)
    result = []
    start = sorted_arr[0][0]
    end = sorted_arr[0][1]
    for i in range(1, length):
        if end >= sorted_arr[i][0]:
            end = max(end, sorted_arr[i][1])
        else:
            result.append([start, end])
            start = sorted_arr[i][0]
            end = sorted_arr[i][1]
    result.append([start, end])
    return result


# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     left = merge_sort(arr[0: len(arr) // 2])
#     right = merge_sort(arr[len(arr) // 2: len(arr)])
#     result = [0] * len(arr)
# 
#     l, r, k = 0, 0, 0
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             result[k] = left[l]
#             l += 1
#         else:
#             result[k] = right[r]
#             r += 1
#         k += 1
# 
#     while l < len(left):
#         result[k] = left[l]
#         l += 1
#         k += 1
#     while r < len(right):
#         result[k] = right[r]
#         r += 1
#         k += 1
# 
#     return result


def __read_input():
    gardeners = int(input())
    flowerbeds = [0] * gardeners
    for i in range(gardeners):
        flowerbeds[i] = list(map(int, input().split()))
    return gardeners, flowerbeds


def main():
    length, arr = __read_input()
    return find_finished_flowerbeds(length, arr)


if __name__ == '__main__':
    arr = main()
    for i in range(len(arr)):
        print(*arr[i])
