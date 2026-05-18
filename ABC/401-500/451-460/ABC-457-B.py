# ABC-457 B - Arrays
# https://atcoder.jp/contests/abc457/tasks/abc457_b
#
def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    LA = [[0]] + getIntListRow(N)
    X, Y = getIntMap()

    print(LA[X][Y])


if __name__ == "__main__":
    main()
