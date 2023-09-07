# ABC-301 B - Fill the Gaps
# https://atcoder.jp/contests/abc301/tasks/abc301_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def d(x, y):
    t = []

    if x < y:
        for i in range(x + 1, y):
            t.append(i)
    else:
        for i in range(y + 1, x):
            t.append(i)
        t.reverse()
    return t


def main():
    n = getInt()
    a = getIntList()

    c = []
    for i in range(1, n):
        x = a[i - 1]
        y = a[i]

        c.append(x)

        if abs(x - y) == 1:
            continue
        else:
            t = d(x, y)
            c = c + t

    c.append(a[-1])

    print(" ".join(map(str, c)))


if __name__ == "__main__":
    main()
