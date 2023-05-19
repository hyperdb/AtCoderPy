# ABC-049 B - たてなが
# https://atcoder.jp/contests/abc049/tasks/abc049_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    h, w = getIntMap()
    d = getStringRow(h)

    for r in d:
        print(r)
        print(r)


if __name__ == "__main__":
    main()
