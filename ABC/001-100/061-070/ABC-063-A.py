# ABC-063 A - Restricted
# https://atcoder.jp/contests/abc063/tasks/abc063_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()
    c = a + b

    print(c if c < 10 else 'error')


if __name__ == "__main__":
    main()
