# ABC-364 A - Glutton Takahashi
# https://atcoder.jp/contests/abc364/tasks/abc364_a
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    r = True
    for i in range(1, N - 1):
        if S[i] == "sweet" and S[i] == S[i - 1]:
            r = False
            break
    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
