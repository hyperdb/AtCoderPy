# ABC-397 A - Thermometer
# https://atcoder.jp/contests/abc397/tasks/abc397_a
#
def getFloat():
    return float(input())


def main():
    X = getFloat()

    print("3" if X < 37.5 else "2" if X < 38.0 else "1")


if __name__ == "__main__":
    main()
