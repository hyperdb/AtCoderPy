# ABC-048 B - Between a and b ...
# https://atcoder.jp/contests/abc048/tasks/abc048_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, x = getIntMap()

    print(((b // x) + 1) if a == 0 else ((b // x) - ((a - 1) // x)))


if __name__ == "__main__":
    main()
