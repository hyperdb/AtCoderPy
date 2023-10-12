# ABC-318 C - Blue Spring
# https://atcoder.jp/contests/abc318/tasks/abc318_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, d, p = getIntMap()
    f = getIntList()
    f = sorted(f, reverse=True) + [0 for _ in range(d)]

    total = sum(f)

    for i in range(len(f) // d):
        s = f[i * d:(i + 1) * d]
        cost = sum(s)
        if cost > p:
            total -= (cost - p)

    print(total)


if __name__ == "__main__":
    main()
