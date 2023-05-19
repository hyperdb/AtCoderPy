# ABC-109 A - ABC333
# https://atcoder.jp/contests/abc109/tasks/abc109_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Yes' if (a * b) % 2 == 1 else 'No')


if __name__ == "__main__":
    main()
