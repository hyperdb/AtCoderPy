# ABC-365 A - Leap Year
# https://atcoder.jp/contests/abc365/tasks/abc365_a
#
def getInt():
    return int(input())


def main():
    Y = getInt()

    if Y % 4 > 0:
        print(365)
    elif Y % 400 == 0:
        print(366)
    elif Y % 100 == 0:
        print(365)
    else:
        print(366)


if __name__ == "__main__":
    main()
