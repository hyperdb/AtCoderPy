# ABC-112 A - Programming Education
# https://atcoder.jp/contests/abc112/tasks/abc112_a
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n = getInt()

    print('Hello World' if n == 1 else sum(getIntRow(n)))


if __name__ == "__main__":
    main()
