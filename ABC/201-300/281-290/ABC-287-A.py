# ABC-287 A - Majority
# https://atcoder.jp/contests/abc287/tasks/abc287_a
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    s = getStringRow(n)

    print('Yes' if s.count('For') > (n / 2) else 'No')


if __name__ == "__main__":
    main()
