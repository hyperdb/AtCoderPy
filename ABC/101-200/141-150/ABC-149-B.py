# ABC-149 B - Greedy Takahashi
# https://atcoder.jp/contests/abc149/tasks/abc149_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, k = getIntMap()

    ax = max(0, a - k)
    bx = max(0, b - max(0, k - a))

    print('%d %d' % (ax, bx))


if __name__ == "__main__":
    main()
