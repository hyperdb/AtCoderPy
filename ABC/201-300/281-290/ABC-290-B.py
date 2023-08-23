# ABC-290 B - Qual B
# https://atcoder.jp/contests/abc290/tasks/abc290_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    n, k = getIntMap()
    s = list(getString())

    j = 0
    for i in range(k):
        j = s.index('o', j)
        j += 1
    print("".join(s[0: j] + ['x' for _ in range(n - j)]))


if __name__ == "__main__":
    main()
