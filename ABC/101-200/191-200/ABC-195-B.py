# ABC-195 B - Many Oranges
# https://atcoder.jp/contests/abc195/tasks/abc195_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, w = getIntMap()

    wg = w * 1000

    c = []
    for i in range(wg // b, (wg // a) + 1):
        if i * a <= wg <= i * b:
            c.append(i)

    print('UNSATISFIABLE' if len(c) == 0 else '%d %d' % (min(c), max(c)))


if __name__ == "__main__":
    main()
