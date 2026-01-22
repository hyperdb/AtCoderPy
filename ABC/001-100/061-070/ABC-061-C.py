# ABC-061 C - Big Array
# https://atcoder.jp/contests/abc061/tasks/abc061_c
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, K = getIntMap()
    ab = getIntListRow(N)

    ab.sort()

    c = 0
    for i in range(N):
        a, b = ab[i]

        c += b
        if c >= K:
            print(a)
            return


if __name__ == "__main__":
    main()
