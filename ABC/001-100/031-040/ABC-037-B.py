# ABC-037 B - 編集
# https://atcoder.jp/contests/abc037/tasks/abc037_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, Q = getIntMap()
    LRT = getIntListRow(Q)
    a = [0 for _ in range(N + 1)]

    for L, R, T in LRT:
        for i in range(L, R + 1):
            a[i] = T

    for i in range(1, len(a)):
        print(a[i])


if __name__ == "__main__":
    main()
