# ABC-193 B - Play Snuke
# https://atcoder.jp/contests/abc193/tasks/abc193_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    l = getIntListRow(n)

    c = -1
    for a, p, x in l:
        if x - a > 0:
            c = p if c == -1 else p if c > p else c
    print(c)


if __name__ == "__main__":
    main()
