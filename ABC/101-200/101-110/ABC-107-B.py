# ABC-107 B - Grid Compression
# https://atcoder.jp/contests/abc107/tasks/abc107_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def transpose(l):
    s = []
    for i in range(len(l[0])):
        r = []
        for j in range(len(l)):
            r.append(l[j][i])
        s.append(r)

    return s


def main():
    h, w = getIntMap()
    a = getStringListRow(h)

    b = transpose(a)

    x = []
    for i in range(len(b)):
        if not '#' in b[i]:
            x.append(i)
    if len(x) > 0:
        x.reverse()
        for i in range(len(a)):
            for j in x:
                a[i].pop(j)

    y = []
    for i in range(len(a)):
        if not '#' in a[i]:
            y.append(i)

    if len(y) > 0:
        y.reverse()
        for j in y:
            a.pop(j)

    for s in a:
        print("".join(s))


if __name__ == "__main__":
    main()
