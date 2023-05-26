# ABC-233 B - A Reverse
# https://atcoder.jp/contests/abc233/tasks/abc233_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    l, r = getIntMap()
    s = getString()

    print(s[:l - 1] + "".join([x for x in reversed(s[l - 1:r])]) + s[r:])


if __name__ == "__main__":
    main()
