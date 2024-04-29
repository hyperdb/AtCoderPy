# ABC-348 A - Penalty Kick
# https://atcoder.jp/contests/abc348/tasks/abc348_a
#
def getInt():
    return int(input())


def main():
    n = getInt()
    r = ['x' if (x + 1) % 3 == 0 else 'o' for x in range(n)]

    print("".join(r))


if __name__ == "__main__":
    main()
