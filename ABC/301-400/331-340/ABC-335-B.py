# ABC-335 B - Tetrahedral Number
# https://atcoder.jp/contests/abc335/tasks/abc335_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    for x in range(n + 1):
        for y in range(n + 1 - x):
            for z in range(n + 1 - x - y):
                print(x, y, z)


if __name__ == "__main__":
    main()
