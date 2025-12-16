# ABC-431 B - Robot Weigh
# https://atcoder.jp/contests/abc431/tasks/abc431_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    X = getInt()
    N = getInt()
    W = [0] + getIntList()
    Q = getInt()
    P = getIntRow(Q)

    attached = [0 for _ in range(N + 1)]
    for p in P:
        if attached[p] == 0:
            attached[p] = W[p]
        else:
            attached[p] = 0
        total = sum(attached) + X
        print(total)


if __name__ == "__main__":
    main()
