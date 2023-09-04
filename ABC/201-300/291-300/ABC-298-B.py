# ABC-298 B - Coloring Matrix
# https://atcoder.jp/contests/abc298/tasks/abc298_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def updown(l):
    result = []

    for i in range(len(l)):
        result.append(l[len(l) - i - 1])

    return result


def rotate(l):
    # upsidedown + transpose -> rotate R

    # upsidedown
    l = updown(l)

    # transpose
    result = []

    for i in range(len(l[0])):
        temp = []
        for v in l:
            temp.append(v[i])
        result.append(temp)
    return result


def check(n, x, y):
    for j in range(n):
        for i in range(n):
            if x[j][i] == 0:
                continue
            if y[j][i] == 1:
                continue
            return False
    return True


def main():
    n = getInt()
    a = getIntListRow(n)
    b = getIntListRow(n)

    r = False
    if check(n, a, b):
        r = True
    else:
        for i in range(3):
            a = rotate(a)
            if check(n, a, b):
                r = True
                break
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
