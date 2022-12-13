# ABC042 B - 文字列大好きいろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_b
#
def getIntList():
    return list(map(int, input().split()))


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    p = getIntList()
    d = getStringRow(p[0])
    d.sort()

    print("".join(d))


if __name__ == "__main__":
    main()
