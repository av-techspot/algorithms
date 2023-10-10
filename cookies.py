def children_pleased(children, greed_lvl, cookies, size):
    greed_lvl = sorted(greed_lvl)
    size = sorted(size)
    counter, i, j = 0, 0, 0
    while (i < children and j < cookies):
        if greed_lvl[i] <= size[j]:
            i += 1
            counter += 1
        j += 1
    return counter


def __read_input():
    children_amount = int(input())
    greed_lvl = list(map(int, input().split()))
    cookies_amount = int(input())
    size = list(map(int, input().split()))
    return children_amount, greed_lvl, cookies_amount, size


def main():
    children, greed_lvl, cookies, size = __read_input()
    return children_pleased(children, greed_lvl, cookies, size)


if __name__ == '__main__':
    print(main())
