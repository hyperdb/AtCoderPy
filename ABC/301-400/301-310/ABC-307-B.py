# ABC-307 B - racecar
# https://atcoder.jp/contests/abc307/tasks/abc307_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def chk(x, y):
    z = x + y
    if z == z[::-1]:
        return True

    z = y + x
    if z == z[::-1]:
        return True
    return False


def main():
    n = getInt()
    s = getStringRow(n)

    r = False
    for i in range(n):
        for j in range(i + 1, n):
            if chk(s[i], s[j]):
                r = True
                break
        if r:
            break
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
