# ABC-128 B - Guidebook
# https://atcoder.jp/contests/abc128/tasks/abc128_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [[input().split(), i + 1] for i in range(N)]


def main():
    n = getInt()
    s = getStringListRow(n)

    for i in range(len(s)):
        s[i][0][1] = 100 - int(s[i][0][1])

    s.sort()

    for d in s:
        print(d[1])


if __name__ == "__main__":
    main()
