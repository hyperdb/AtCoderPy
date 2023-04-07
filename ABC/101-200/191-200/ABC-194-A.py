# ABC-194 A - I Scream
# https://atcoder.jp/contests/abc194/tasks/abc194_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    t = 4
    if a + b >= 15 and b >= 8:
        t = 1
    elif a + b >= 10 and b >= 3:
        t = 2
    elif a + b >= 3:
        t = 3
    print(t)


if __name__ == "__main__":
    main()
