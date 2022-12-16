# ABC-048 B - Between a and b ...
# https://atcoder.jp/contests/abc048/tasks/abc048_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, x = getIntMap()

    c = 0
    if a == 0:
        c = (b // x) + 1
    else:
        c = (b // x) - ((a - 1) // x)
    print(c)


if __name__ == "__main__":
    main()
