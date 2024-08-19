# ABC-359 A - Count Takahashi
# https://atcoder.jp/contests/abc359/tasks/abc359_a
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    print(S.count('Takahashi'))


if __name__ == "__main__":
    main()
