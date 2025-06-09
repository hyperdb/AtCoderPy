# ABC-408 C - Not All Covered
# https://atcoder.jp/contests/abc408/tasks/abc408_c
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    LR = getIntListRow(M)

    C = [0 for _ in range(N + 1)]

    # imos法
    for l, r in LR:
        C[l] += 1
        if r + 1 <= N:
            C[r + 1] -= 1

    n = 0
    ans = N + 1
    for i in range(1, N + 1):
        n += C[i]
        ans = min(ans, n)

    print(ans)


if __name__ == "__main__":
    main()
