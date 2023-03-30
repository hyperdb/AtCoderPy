# ABC-186 B - Blocks on Grid
# https://atcoder.jp/contests/abc186/tasks/abc186_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    h, w = getIntMap()
    a = getIntListRow(h)

    m = min([min(l) for l in a])
    s = sum([sum(l) for l in a])

    print(s - (m * h * w))


if __name__ == "__main__":
    main()
