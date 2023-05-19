# ABC-138 A - Red or Not
# https://atcoder.jp/contests/abc138/tasks/abc138_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    a = getInt()
    s = getString()

    print(s if a >= 3200 else 'red')


if __name__ == "__main__":
    main()
