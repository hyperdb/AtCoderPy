# ABC-323 B - Round-Robin Tournament
# https://atcoder.jp/contests/abc323/tasks/abc323_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    n = getInt()
    s = getStringRow(n)

    entry = {}
    for i in range(n):
        entry[i + 1] = s[i].count('o') * 1000 + (n - i)

    result = sorted(entry.items(), key=lambda players: players[1], reverse=True)

    print(" ".join([str(x) for x, y in result]))


if __name__ == "__main__":
    main()
