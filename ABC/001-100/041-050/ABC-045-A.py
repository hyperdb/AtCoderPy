# ABC-045 A - 台形
# https://atcoder.jp/contests/abc045/tasks/abc045_a
#
def getInt():
    return int(input())


def main():
    a = getInt()
    b = getInt()
    h = getInt()

    print(int((a + b) * h / 2))


if __name__ == "__main__":
    main()
