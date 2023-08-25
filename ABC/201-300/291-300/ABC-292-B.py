# ABC-292 B - Yellow and Red Card
# https://atcoder.jp/contests/abc292/tasks/abc292_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, q = getIntMap()
    ev = getIntListRow(q)
    c = [0] + [0 for _ in range(n)]

    for i, x in ev:
        if i == 3:
            print('Yes' if c[x] >= 2 else 'No')
        else:
            c[x] += i


if __name__ == "__main__":
    main()
