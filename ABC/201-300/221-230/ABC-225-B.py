# ABC-225 B - Star or Not
# https://atcoder.jp/contests/abc225/tasks/abc225_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    ab = getIntListRow(n - 1)

    c = [0 for _ in range(0, n + 1)]

    for a, b in ab:
        c[a] += 1
        c[b] += 1

    print('Yes' if max(c) == n - 1 else 'No')


if __name__ == "__main__":
    main()
