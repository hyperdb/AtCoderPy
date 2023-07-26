# ABC-272 B - Everyone is Friends
# https://atcoder.jp/contests/abc272/tasks/abc272_b
#
import itertools


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    k = getIntListRow(m)

    a = sum([i + 1 for i in range(n - 1)])

    c = []
    for x in range(m):
        c += list(itertools.combinations(k[x][1:], 2))

    print('Yes' if a == len(set(c)) else 'No')


if __name__ == "__main__":
    main()
