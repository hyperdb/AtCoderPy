# ABC-213 B - Booby Prize
# https://atcoder.jp/contests/abc213/tasks/abc213_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    b = dict()
    for i in range(n):
        b[a[i]] = i + 1
    c = sorted(b.items())

    print(c[n - 2][1])


if __name__ == "__main__":
    main()
