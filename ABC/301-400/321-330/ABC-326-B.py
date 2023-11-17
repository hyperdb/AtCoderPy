# ABC-326 B - 326-like Numbers
# https://atcoder.jp/contests/abc326/tasks/abc326_b
#
def getInt():
    return int(input())


def checkNum(x):
    a, b, c = map(int, list(str(x)))

    return (True if a * b == c else False)


def main():
    n = getInt()

    for i in range(n, 920):
        if checkNum(i):
            print(i)
            break


if __name__ == "__main__":
    main()
