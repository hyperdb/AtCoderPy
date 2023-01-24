# A - Rated for Me
# https://atcoder.jp/contests/abc104/tasks/abc104_a
#
def getInt():
    return int(input())


def main():
    r = getInt()

    print('ABC' if r < 1200 else 'ARC' if r < 2800 else 'AGC')


if __name__ == "__main__":
    main()
