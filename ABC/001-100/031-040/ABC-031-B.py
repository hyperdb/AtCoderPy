# ABC-031 B - 運動管理
# https://atcoder.jp/contests/abc031/tasks/abc031_b
#
def getIntMap():
    return map(int, input().split())


def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    L, H = getIntMap()
    N = getInt()
    A = getIntRow(N)

    for d in A:
        if L <= d <= H:
            print(0)
        elif d >= H:
            print(-1)
        else:
            print(L - d)


if __name__ == "__main__":
    main()
