# ABC-341 B - Foreign Exchange
# https://atcoder.jp/contests/abc341/tasks/abc341_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    a = [0] + getIntList()
    st = [[0, 0]] + getIntListRow(n - 1)

    # a[i] -> a[i+1] に最大数転送する
    for i in range(1, n):
        s, t = st[i]
        d, m = divmod(a[i], s)

        a[i + 1] += d * t
        a[i] = m

    print(a[-1])


if __name__ == "__main__":
    main()
