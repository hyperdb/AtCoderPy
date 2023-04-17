# ABC-203 B - AtCoder Condominium
# https://atcoder.jp/contests/abc203/tasks/abc203_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, k = getIntMap()

    a = (1 + k) * k // 2
    b = k * 100

    t = 0
    for i in range(1, n + 1):
        t += (a + b * i)
    print(t)


if __name__ == "__main__":
    main()
