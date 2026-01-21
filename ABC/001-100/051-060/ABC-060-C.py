# ABC-060 C - Sentou
# https://atcoder.jp/contests/abc060/tasks/arc073_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, T = getIntMap()
    t = getIntList()

    total = 0
    for i in range(1, N):
        d = t[i] - t[i - 1]
        # 前回からの時間差がT未満の場合は時間差分だけ加算
        total += min(d, T)
    # 最後の1回分を加算
    total += T

    print(total)


if __name__ == "__main__":
    main()
