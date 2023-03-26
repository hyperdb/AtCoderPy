# ABC-182 A - twiblr
# https://atcoder.jp/contests/abc182/tasks/abc182_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(max((a * 2 + 100) - b, 0))


if __name__ == "__main__":
    main()
