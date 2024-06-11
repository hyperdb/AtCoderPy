# ABC-093 B - Small and Large Integers
# https://atcoder.jp/contests/abc093/tasks/abc093_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, x = getIntMap()

    if x >= (b - a) + 1:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, a + x):
            print(i)
        for i in range(b - x + 1, b + 1):
            if i >= (a + x):
                print(i)


if __name__ == "__main__":
    main()
