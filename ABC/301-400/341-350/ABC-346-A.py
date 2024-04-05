# ABC-346 A - Adjacent Product
# https://atcoder.jp/contests/abc346/tasks/abc346_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    b = []

    for i in range(1, n):
        b.append(a[i - 1] * a[i])

    print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()
