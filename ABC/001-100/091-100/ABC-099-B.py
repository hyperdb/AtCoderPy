# ABC-099 B - Stone Monument
# https://atcoder.jp/contests/abc099/tasks/abc099_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = b - a - 1
    x = (1 + c) * c // 2

    print(x - a)


if __name__ == "__main__":
    main()
