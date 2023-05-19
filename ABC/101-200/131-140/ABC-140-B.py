# ABC-140 B - Buffet
# https://atcoder.jp/contests/abc140/tasks/abc140_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    b = getIntList()
    c = getIntList()

    s = 0
    l = n
    for i in range(n):
        s += b[a[i] - 1]
        if l == a[i] - 1:
            s += c[l - 1]
        l = a[i]
    print(s)


if __name__ == "__main__":
    main()
