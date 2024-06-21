# ABC-036 B - 回転
# https://atcoder.jp/contests/abc036/tasks/abc036_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    for i in range(N):
        t = []
        for j in range(N):
            t.append(S[j][i])
        t.reverse()
        print("".join(t))


if __name__ == "__main__":
    main()
