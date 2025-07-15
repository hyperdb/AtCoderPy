# ABC-413 B - cat 2
# https://atcoder.jp/contests/abc413/tasks/abc413_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    T = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            T.add(S[i] + S[j])

    print(len(T))


if __name__ == "__main__":
    main()
