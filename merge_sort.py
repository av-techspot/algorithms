# unfinished

def merge(arr, lf, mid, rg):
    pass


def merge_sort(arr, lf, rg):
    if len(arr) == 1:
        return arr
    mid = (lf + rg) // 2
    left = merge_sort(arr, lf, mid)
    right = merge_sort(arr, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
