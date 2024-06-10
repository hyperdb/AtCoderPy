# ABC042 B - 文字列大好きいろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N, L = getIntMap()
    S = getStringRow(N)
    S.sort()

    print("".join(S))


if __name__ == "__main__":
    main()
