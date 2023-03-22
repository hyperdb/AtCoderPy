# ABC-178 B - Product Max
# https://atcoder.jp/contests/abc178/tasks/abc178_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    print(max(max(a * c, a * d), max(b * c, b * d)))


if __name__ == "__main__":
    main()
