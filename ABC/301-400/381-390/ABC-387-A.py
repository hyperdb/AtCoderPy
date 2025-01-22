# ABC-387 A - Happy New Year 2025
# https://atcoder.jp/contests/abc387/tasks/abc387_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B = getIntMap()

    print((A + B) ** 2)


if __name__ == "__main__":
    main()
