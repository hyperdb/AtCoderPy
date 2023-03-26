# ABC-181 A - Heavy Rotation
# https://atcoder.jp/contests/abc181/tasks/abc181_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print('White' if n % 2 == 0 else 'Black')


if __name__ == "__main__":
    main()
