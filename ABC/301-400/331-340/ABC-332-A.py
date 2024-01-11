# ABC-332 A - Online Shopping
# https://atcoder.jp/contests/abc332/tasks/abc332_a
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, s, k = getIntMap()
    pq = getIntListRow(n)
    p = sum([x * y for x, y in pq])

    print(p + (k if p < s else 0))


if __name__ == "__main__":
    main()
