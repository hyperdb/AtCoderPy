# ABC-253 A - Median?
# https://atcoder.jp/contests/abc253/tasks/abc253_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    l = [a, b, c]
    l.sort()

    print('Yes' if l[1] == b else 'No')


if __name__ == "__main__":
    main()
