# ABC-136 A - Transfer
# https://atcoder.jp/contests/abc136/tasks/abc136_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    d = a - b

    print(0 if d > c else c - d)


if __name__ == "__main__":
    main()
