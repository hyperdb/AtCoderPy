# ABC-234 B - Longest Segment
# https://atcoder.jp/contests/abc234/tasks/abc234_b
#
import math
import itertools

def getInt():
    return int(input())

def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]

def d(x, y):
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

def main():
    n = getInt()
    xy = getIntListRow(n)

    r = 0.0
    for a, b in itertools.combinations([i for i in range(n)], 2):
        r = max(r, d(xy[a], xy[b]))
    print(r)

if __name__ == "__main__":
    main()
