# ABC-423 A - Scary Fee
# https://atcoder.jp/contests/abc423/tasks/abc423_a
#
def getIntMap():
    return map(int, input().split())


def main():
    X, C = getIntMap()

    k = X // (1000 + C)

    print(k * 1000)


if __name__ == "__main__":
    main()
