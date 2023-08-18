# ABC-287 B - Postal Card
# https://atcoder.jp/contests/abc287/tasks/abc287_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n, m = getIntMap()
    s = getStringRow(n)
    t = getStringRow(m)

    r = [w[-3:] for w in s]

    c = 0
    for w in r:
        if w in t:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
