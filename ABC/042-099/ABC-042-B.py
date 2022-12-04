# ABC042 B - 文字列大好きいろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_b
#
def getIntList():
    return list(map(int, input().split()))


def getStringRow(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def main():
    param = getIntList()
    data = getStringRow(param[0])

    data.sort()

    print("".join(data))


if __name__ == "__main__":
    main()
