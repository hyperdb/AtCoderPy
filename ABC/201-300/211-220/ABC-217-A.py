# ABC-217 A - Lexicographic Order
# https://atcoder.jp/contests/abc217/tasks/abc217_a
#
def getStringList():
    return list(input().split())


def main():
    s = getStringList()
    t = sorted(s)

    print('Yes' if s[0] == t[0] else 'No')


if __name__ == "__main__":
    main()
