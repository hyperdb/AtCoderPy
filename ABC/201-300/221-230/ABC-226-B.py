# ABC-226 B - Counting Arrays
# https://atcoder.jp/contests/abc226/tasks/abc226_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    l = getStringRow(n)

    print(len(set(l)))


if __name__ == "__main__":
    main()
