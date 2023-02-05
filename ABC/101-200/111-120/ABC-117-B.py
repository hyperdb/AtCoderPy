# ABC-117 B - Polygon
# https://atcoder.jp/contests/abc117/tasks/abc117_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    l = getIntList()

    l.sort()

    m = l[n - 1]
    l.pop(n - 1)

    print('Yes' if sum(l) > m else 'No')


if __name__ == "__main__":
    main()
