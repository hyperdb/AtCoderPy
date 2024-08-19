# ABC-361 B - Intersection of Cuboids
# https://atcoder.jp/contests/abc361/tasks/abc361_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d, e, f = getIntMap()
    g, h, i, j, k, l = getIntMap()

    r = True
    if max(a, g) >= min(d, j):
        r = False
    elif max(b, h) >= min(e, k):
        r = False
    elif max(c, i) >= min(f, l):
        r = False

    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
