# ABC-046 B - AtCoDeerくんとボール色塗り
# https://atcoder.jp/contests/abc046/tasks/abc046_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, k = getIntMap()

    if n == 1:
        print(k)
    else:
        v = k
        for i in range(n - 1):
            v = v * (k - 1)
        print(v)


if __name__ == "__main__":
    main()
