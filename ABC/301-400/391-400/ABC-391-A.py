# ABC-391 A - Lucky Direction
# https://atcoder.jp/contests/abc391/tasks/abc391_a
#
def getString():
    return input()


def main():
    S = getString()
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    i = dirs.index(S)

    print(dirs[(i + 4) % 8])


if __name__ == "__main__":
    main()
