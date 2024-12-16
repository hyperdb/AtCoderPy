# ABC-383 A - Humidifier 1
# https://atcoder.jp/contests/abc383/tasks/abc383_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    TV = getIntListRow(N)

    c = 0
    e = 0
    for T, V in TV:
        c -= T - e
        c = max(c, 0)
        c += V
        e = T
    print(c)


if __name__ == "__main__":
    main()
