# ABC-384 B - ARC Division
# https://atcoder.jp/contests/abc384/tasks/abc384_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def check(d, r):
    return 1600 <= r <= 2799 if d == 1 else 1200 <= r <= 2399


def main():
    N, R = getIntMap()
    DA = getIntListRow(N)

    for D, A in DA:
        R += A if check(D, R) else 0

    print(R)


if __name__ == "__main__":
    main()
