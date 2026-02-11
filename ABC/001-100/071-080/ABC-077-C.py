# ABC-077 C - Snuke Festival
# https://atcoder.jp/contests/abc077/tasks/arc084_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


# 2分探索
def binary_search(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def main():
    N = getInt()
    A = getIntList()
    B = getIntList()
    C = getIntList()

    A.sort()
    B.sort()
    C.sort()

    pattern = 0
    for i in range(N):
        b = B[i]

        a = binary_search(A, b)
        c = N - binary_search(C, b + 1)

        pattern += a * c

    print(pattern)


if __name__ == "__main__":
    main()
