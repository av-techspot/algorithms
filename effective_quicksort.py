# id 87428897

def quicksort(participants, start, end):
    if start >= end:
        return

    pivot = participants[(start + end) // 2]
    start_shift, end_shift = start, end
    while start_shift <= end_shift:
        while participants[start_shift] < pivot:
            start_shift += 1
        while participants[end_shift] > pivot:
            end_shift -= 1
        participants[start_shift], participants[end_shift] = participants[end_shift], participants[start_shift]
        start_shift += 1
        end_shift -= 1
    quicksort(participants, start, end_shift)
    quicksort(participants, start_shift, end)


def main():
    length, participants = __read_input()
    quicksort(participants, 0, length-1)
    for p in participants:
        _, _, login = p
        print(login)


if __name__ == '__main__':
    def __read_input():
        length = int(input())
        participants = [0] * length
        for i in range(0, length):
            login, points, faults = input().split()
            participants[i] = (-int(points), int(faults), login)
        return length, participants

    main()
