# ABC-249 A - Jogging
# https://atcoder.jp/contests/abc249/tasks/abc249_a
#
def getIntMap():
    return map(int, input().split())


def run(a, b, c, x):
    r = 0
    while x > 0:
        r += (a if x > a else x) * b
        x -= (a + c)
    return r


def main():
    a, b, c, d, e, f, x = getIntMap()

    ta = run(a, b, c, x)
    ao = run(d, e, f, x)

    print('Draw' if ta == ao else 'Takahashi' if ta > ao else 'Aoki')


if __name__ == "__main__":
    main()
