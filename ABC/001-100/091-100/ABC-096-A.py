# ABC-096 A - Day of Takahashi
# https://atcoder.jp/contests/abc096/tasks/abc096_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(a if b >= a else a - 1)


if __name__ == "__main__":
    main()
