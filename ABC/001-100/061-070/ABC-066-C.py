# ABC-066 C - pushpush
# https://atcoder.jp/contests/abc066/tasks/arc077_a
#
# 両端のアクセスならキュー（deque）が便利
from collections import deque


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()
    B = deque()

    for i in range(N):
        if i % 2 == 0:
            B.append(a[i])
        else:
            B.appendleft(a[i])

    if N % 2 == 1:
        B.reverse()

    print(" ".join(map(str, B)))


if __name__ == "__main__":
    main()
