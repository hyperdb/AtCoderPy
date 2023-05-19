# ABC-181 B - Trapezoid Sum
# https://atcoder.jp/contests/abc181/tasks/abc181_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    l = getIntListRow(n)

    s = 0
    for a, b in l:
        c = b - a + 1
        s += (a + b) * c // 2
    print(s)


if __name__ == "__main__":
    main()
