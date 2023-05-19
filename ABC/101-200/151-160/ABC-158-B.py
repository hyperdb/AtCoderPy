# ABC-158 B - Count Balls
# https://atcoder.jp/contests/abc158/tasks/abc158_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, a, b = getIntMap()

    c = n // (a + b) * a

    m = n % (a + b)
    c += m if m <= a else a

    print(c)


if __name__ == "__main__":
    main()
