# ABC-037 C - 総和
# https://atcoder.jp/contests/abc037/tasks/abc037_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    a = getIntList()

    s = 0
    # 各項のk個分の合計を求める
    for i in range(n):
        s += a[i] * k
    # 両端の余計に加算した部分を引く
    for i in range(k):
        s -= a[i] * (k - (i + 1))
        s -= a[-1 - i] * (k - (i + 1))

    print(s)


if __name__ == "__main__":
    main()
