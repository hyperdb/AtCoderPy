# ABC-041 B - 直方体
# https://atcoder.jp/contests/abc041/tasks/abc041_b
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C = getIntMap()
    x = A * B * C
    d = 10**9 + 7

    print(x % d)


if __name__ == "__main__":
    main()
