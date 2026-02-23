# ABC-445 B - Center Alignment
# https://atcoder.jp/contests/abc445/tasks/abc445_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)
    L = [len(s) for s in S]

    maxL = max(L)

    for i in range(N):
        if L[i] == maxL:
            print(S[i])
        else:
            dots = "." * ((maxL - L[i]) // 2)
            print(dots + S[i] + dots)


if __name__ == "__main__":
    main()
