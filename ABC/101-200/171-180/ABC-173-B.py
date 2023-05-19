# ABC-173 B - Judge Status Summary
# https://atcoder.jp/contests/abc173/tasks/abc173_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    s = getStringRow(n)

    a = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

    for r in s:
        a[r] += 1

    for k, v in a.items():
        print('%s x %d' % (k, v))


if __name__ == "__main__":
    main()
