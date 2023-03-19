# ABC-174 B - Distance
# https://atcoder.jp/contests/abc174/tasks/abc174_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, d = getIntMap()
    l = getIntListRow(n)

    d = d ** 2

    c = 0
    for x, y in l:
        if d >= (x ** 2 + y ** 2):
            c += 1
    print(c)


if __name__ == "__main__":
    main()
