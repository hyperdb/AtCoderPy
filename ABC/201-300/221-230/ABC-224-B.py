# ABC-224 B - Mongeness
# https://atcoder.jp/contests/abc224/tasks/abc224_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    h, w = getIntMap()
    a = getIntListRow(h)

    f = True
    for y in range(h - 1):
        for x in range(w - 1):
            for i in range(x + 1, w):
                p1 = a[y][x]
                q1 = a[y + 1][i]

                p2 = a[y + 1][x]
                q2 = a[y][i]
                if p1 + q1 > p2 + q2:
                    f = False
                    break
    print('Yes' if f else 'No')


if __name__ == "__main__":
    main()
