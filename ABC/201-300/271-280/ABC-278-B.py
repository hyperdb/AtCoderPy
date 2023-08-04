# ABC-278 B - Misjudge the Time
# https://atcoder.jp/contests/abc278/tasks/abc278_b
#
def getIntMap():
    return map(int, input().split())


def c(h, m):
    x = list('%02d' % h)
    y = list('%02d' % m)

    nh = x[0] + y[0]
    nm = x[1] + y[1]

    return True if ('00' <= nh <= '23') and ('00' <= nm <= '59') else False


def a(h, m):
    m += 1
    if m > 59:
        h += 1
        m = 0
    if h > 23:
        h = 0
    return h, m


def main():
    h, m = getIntMap()

    while not c(h, m):
        h, m = a(h, m)

    print(h, m)


if __name__ == "__main__":
    main()
