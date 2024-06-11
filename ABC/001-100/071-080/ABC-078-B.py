# ABC-078 B - ISU
# https://atcoder.jp/contests/abc078/tasks/abc078_b
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y, z = getIntMap()

    print((x - z) // (y + z))


if __name__ == "__main__":
    main()
