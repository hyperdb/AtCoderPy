# ABC-059 B - Comparison
# https://atcoder.jp/contests/abc059/tasks/abc059_b
#
def getInt():
    return int(input())


def main():
    a = getInt()
    b = getInt()

    print('GREATER' if a > b else 'LESS' if a < b else 'EQUAL')


if __name__ == "__main__":
    main()
