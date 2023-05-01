# ABC-216 B - Same Name
# https://atcoder.jp/contests/abc216/tasks/abc216_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    st = getStringRow(n)

    print('Yes' if len(set(st)) < n else 'No')


if __name__ == "__main__":
    main()
