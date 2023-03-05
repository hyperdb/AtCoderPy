# ABC-157 B - Bingo
# https://atcoder.jp/contests/abc157/tasks/abc157_b
#
def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def check(a):
    for i in range(3):
        if sum(a[i]) == 0:
            return True
    for j in range(3):
        if sum([a[0][j], a[1][j], a[2][j]]) == 0:
            return True
    if sum([a[0][0], a[1][1], a[2][2]]) == 0:
        return True
    if sum([a[2][0], a[1][1], a[0][2]]) == 0:
        return True
    return False


def main():
    a = getIntListRow(3)
    n = getInt()
    b = getIntRow(n)

    for c in b:
        for i in range(3):
            for j in range(3):
                if a[i][j] == c:
                    a[i][j] = 0
    print('Yes' if check(a) else 'No')


if __name__ == "__main__":
    main()
