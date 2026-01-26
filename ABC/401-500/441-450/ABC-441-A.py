# ABC-441 A - Black Square
# https://atcoder.jp/contests/abc441/tasks/abc441_a
#
def getIntMap():
    return map(int, input().split())


def main():
    P, Q = getIntMap()
    X, Y = getIntMap()

    if P <= X < P + 100 and Q <= Y < Q + 100:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
