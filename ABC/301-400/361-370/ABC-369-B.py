# ABC-369 B - Piano 3
# https://atcoder.jp/contests/abc369/tasks/abc369_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    N = getInt()
    AS = getStringListRow(N)

    L = [int(AS[i][0]) for i in range(N) if AS[i][1] == "L"]
    R = [int(AS[i][0]) for i in range(N) if AS[i][1] == "R"]

    t = 0
    if len(L) > 1:
        for i in range(1, len(L)):
            t += abs(L[i] - L[i - 1])
    if len(R) > 1:
        for i in range(1, len(R)):
            t += abs(R[i] - R[i - 1])
    print(t)


if __name__ == "__main__":
    main()
