# ABC-050 A - Addition and Subtraction Easy
# https://atcoder.jp/contests/abc050/tasks/abc050_a
#
def getStringMap():
    return input().split()


def main():
    a, op, b = getStringMap()

    c = 1 if (op == '+') else -1

    print(int(a) + (c * int(b)))


if __name__ == "__main__":
    main()
