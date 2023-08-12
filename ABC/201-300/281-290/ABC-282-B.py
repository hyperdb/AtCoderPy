# ABC-282 B - Let's Get a Perfect Score
# https://atcoder.jp/contests/abc282/tasks/abc282_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def chk(a1, a2):
    r = True
    for i in range(len(a1)):
        if a1[i] == 'x' and a2[i] == 'x':
            r = False
            break
    return r


def main():
    n, m = getIntMap()
    s = getStringListRow(n)

    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if chk(s[i], s[j]):
                c += 1
    print(c)


if __name__ == "__main__":
    main()
