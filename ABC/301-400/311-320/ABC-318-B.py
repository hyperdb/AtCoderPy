# ABC-318 B - Overlapping sheets
# https://atcoder.jp/contests/abc318/tasks/abc318_b
#
def getInt():
    return int(input())

def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]

def getMax(xy):
    m = 0
    for x in xy:
        m = max(m, max(x))
    return m

def getSum(xy):
    s = 0
    for x in xy:
        s += sum(x)
    return s

def main():
    n = getInt()
    abcd = getIntListRow(n)

    m = getMax(abcd)

    r = [[0 for _ in range(m)] for _ in range(m)]

    for a, b, c, d in abcd:
        for x in range(a, b):
            for y in range(c, d):
                r[y][x] = 1

    print(getSum(r))

if __name__ == "__main__":
    main()