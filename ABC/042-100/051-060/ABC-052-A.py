# ABC-052 A - Two Rectangles
# https://atcoder.jp/contests/abc052/tasks/abc052_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    print(a * b if a * b >= c * d else c * d)


if __name__ == "__main__":
    main()
