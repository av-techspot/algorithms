#id 86029106

def main():
    street_length = int(input())
    houses = [int(x) for x in input().split()]

    left = 0
    right = 0
    result = [street_length] * street_length
    for i in range(len(houses)):
        if houses[i] == 0:
            result[i] = 0
            j = i - 1
            left = 1
            while j >= 0 and result[j] > left:
                result[j] = left
                j -= 1
                left += 1
            right = 0
            left = 0
        if houses[i] != 0 and houses[abs(i-1-right)] == 0:
            right += 1
            result[i] = right

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
