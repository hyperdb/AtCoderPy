# ABC-388 B - Heavy Snake
# https://atcoder.jp/contests/abc388/tasks/abc388_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, D = getIntMap()
    TL = getIntListRow(N)

    for i in range(1, D + 1):
        w = 0
        for T, L in TL:
            w = max(w, T * (L + i))
        print(w)


if __name__ == "__main__":
    main()
