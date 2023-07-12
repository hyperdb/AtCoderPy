# ABC-264 B - Nice Grid
# https://atcoder.jp/contests/abc264/tasks/abc264_b
#
def getIntMap():
    return map(int, input().split())


def main():
    r, c = getIntMap()

    d = max(abs(r - 8), abs(c - 8))

    print('white' if d % 2 == 0 else 'black')


if __name__ == "__main__":
    main()
