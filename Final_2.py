# id 86143472

def main():
    k = int(input()) * 2
    lines = ''
    for line in range(4):
        line = input()
        lines += line
    lines = lines.replace('.', '')
    counter = [0] * 10
    points = 0
    i = 1
    for i in lines:
        counter[int(i)] += 1
    for i in counter:
        if 0 < i <= k:
            points += 1
    print(points)


if __name__ == '__main__':
    main()
