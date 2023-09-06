# ABC-300 B - Same Map in the RPG World
# https://atcoder.jp/contests/abc300/tasks/abc300_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def rx(x):
    for i in range(len(x)):
        x[i] = x[i][1:] + x[i][:1]
    return x


def ry(x):
    return x[1:] + x[:1]


def main():
    h, w = getIntMap()
    a = getStringListRow(h)
    b = getStringListRow(h)

    if a == b:
        print('Yes')
    else:
        r = False
        c = a
        for j in range(h):
            d = c
            for i in range(w):
                if b == d:
                    r = True
                    break
                d = rx(d)
            if r:
                break
            c = ry(c)

        print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
