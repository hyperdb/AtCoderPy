# ABC-054 B - Template Matching
# https://atcoder.jp/contests/abc054/tasks/abc054_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def check_area(rectangle, template, i, j):
    for x in range(len(template)):
        for y in range(len(template)):
            if rectangle[i + x][j + y] != template[x][y]:
                return False
    return True


def main():
    n, m = getIntMap()
    a = getStringRow(n)
    b = getStringRow(m)

    f = False
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if check_area(a, b, i, j):
                f = True
                break
        if f:
            break
    print('Yes' if f else 'No')


if __name__ == "__main__":
    main()
