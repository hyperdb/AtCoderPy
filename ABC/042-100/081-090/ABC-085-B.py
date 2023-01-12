# ABC-085 B - Kagami Mochi
# https://atcoder.jp/contests/abc085/tasks/abc085_b
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n = getInt()
    d = getIntRow(n)

    r = set(d)

    print(len(r))


if __name__ == "__main__":
    main()
