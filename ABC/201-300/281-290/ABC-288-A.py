# ABC-288 A - Many A+B Problems
# https://atcoder.jp/contests/abc288/tasks/abc288_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    ab = getIntListRow(n)

    for c in ab:
        print(sum(c))


if __name__ == "__main__":
    main()
