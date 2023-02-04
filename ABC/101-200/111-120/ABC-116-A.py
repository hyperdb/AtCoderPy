# ABC-116 A - Right Triangle
# https://atcoder.jp/contests/abc116/tasks/abc116_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    print(a * b // 2)


if __name__ == "__main__":
    main()
