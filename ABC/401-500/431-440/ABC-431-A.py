# ABC-431 A - Robot Balance
# https://atcoder.jp/contests/abc431/tasks/abc431_a
#
def getIntMap():
    return map(int, input().split())


def main():
    H, B = getIntMap()

    print(0 if H < B else H - B)


if __name__ == "__main__":
    main()
