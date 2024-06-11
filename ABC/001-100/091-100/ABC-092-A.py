# ABC-092 A - Traveling Budget
# https://atcoder.jp/contests/abc092/tasks/abc092_a
#
def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    a, b, c, d = getIntRow(4)

    print((a if a < b else b) + (c if c < d else d))


if __name__ == "__main__":
    main()
