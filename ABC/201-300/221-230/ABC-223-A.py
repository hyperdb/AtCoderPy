# ABC-223 A - Exact Price
# https://atcoder.jp/contests/abc223/tasks/abc223_a
#
def getInt():
    return int(input())


def main():
    x = getInt()

    print('No' if x == 0 or x % 100 > 0 else 'Yes')


if __name__ == "__main__":
    main()
