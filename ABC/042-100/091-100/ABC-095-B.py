# ABC-095 B - Bitter Alchemy
# https://atcoder.jp/contests/abc095/tasks/abc095_b
#
def getIntMap():
    return map(int, input().split())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n, x = getIntMap()
    m = getIntRow(n)

    m.sort()

    c = len(m)
    x -= sum(m)
    c += x // m[0]

    print(c)


if __name__ == "__main__":
    main()
