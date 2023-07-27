# ABC-273 B - Broken Rounding
# https://atcoder.jp/contests/abc273/tasks/abc273_b
#
def getIntMap():
    return map(int, input().split())


def r(a, b):
    a += (5 * (10 ** b))
    b += 1
    return a // (10 ** b) * (10 ** b)


def main():
    x, k = getIntMap()

    for i in range(k):
        x = r(x, i)
    print(x)


if __name__ == "__main__":
    main()
