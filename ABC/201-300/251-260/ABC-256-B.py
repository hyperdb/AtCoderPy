# ABC-256 B - Batters
# https://atcoder.jp/contests/abc256/tasks/abc256_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def shift_one(x):
    y = [0 for _ in range(len(x))]
    for i in range(len(x) - 1):
        y[i + 1] = x[i]
    return y


def main():
    n = getInt()
    a = getIntList()

    p = 0
    b = [0, 0, 0, 0, 0]
    for h in a:
        b[0] = 1
        for i in range(h):
            b = shift_one(b)
            if b[4] > 0:
                p += 1
    print(p)


if __name__ == "__main__":
    main()
