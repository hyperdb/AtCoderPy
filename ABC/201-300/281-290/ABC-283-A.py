# ABC-283 A - Power
# https://atcoder.jp/contests/abc283/tasks/abc283_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(a ** b)


if __name__ == "__main__":
    main()
