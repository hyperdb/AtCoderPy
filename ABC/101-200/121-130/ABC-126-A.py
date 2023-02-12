# ABC-126 A - Changing a Character
# https://atcoder.jp/contests/abc126/tasks/abc126_a
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    n, k = getIntMap()
    s = list(getString())

    s[k - 1] = s[k - 1].lower()

    print("".join(s))


if __name__ == "__main__":
    main()
