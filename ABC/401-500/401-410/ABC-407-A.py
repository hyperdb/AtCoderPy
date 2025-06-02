# ABC-407 A - Approximation
# https://atcoder.jp/contests/abc407/tasks/abc407_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B = getIntMap()

    d, m = divmod(A, B)

    if m == 0:
        print(d)
    elif B < m * 2:  # near d + 1
        print(d + 1)
    else:
        print(d)


if __name__ == "__main__":
    main()
