# ABC-193 A - Discount
# https://atcoder.jp/contests/abc193/tasks/abc193_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print((a - b) / a * 100)


if __name__ == "__main__":
    main()
