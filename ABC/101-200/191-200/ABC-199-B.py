# ABC-199 B - Intersection
# https://atcoder.jp/contests/abc199/tasks/abc199_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    b = getIntList()

    c = min(b) - max(a) + 1

    print(c if c > 0 else 0)


if __name__ == "__main__":
    main()
