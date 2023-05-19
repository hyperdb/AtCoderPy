# ABC-056 B - NarrowRectanglesEasy
# https://atcoder.jp/contests/abc056/tasks/abc056_b
#
def getIntMap():
    return map(int, input().split())


def main():
    w, a, b = getIntMap()

    d = b - (a + w) if b > a else a - (b + w)
    print(d if d >= 0 else 0)


if __name__ == "__main__":
    main()
