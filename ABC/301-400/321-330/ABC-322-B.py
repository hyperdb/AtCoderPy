# ABC-322 B - Prefix and Suffix
# https://atcoder.jp/contests/abc322/tasks/abc322_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    n, m = getIntMap()
    s = getString()
    t = getString()

    f = 3
    f -= (2 if t[:n] == s else 0)
    f -= (1 if t[-1 * n:] == s else 0)

    print(f)


if __name__ == "__main__":
    main()
