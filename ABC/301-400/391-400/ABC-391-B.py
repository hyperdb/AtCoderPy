# ABC-391 B - Seek Grid
# https://atcoder.jp/contests/abc391/tasks/abc391_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N, M = getIntMap()
    S = getStringRow(N)
    T = getStringRow(M)

    target = "".join(T)

    limit = N - M + 1

    r = False
    for a in range(limit):
        for b in range(limit):
            src = ""
            for z in range(M):
                src += S[a + z][b : b + M]

            if src == target:
                print(a + 1, b + 1)
                r = True

            if r:
                break
        if r:
            break


if __name__ == "__main__":
    main()
