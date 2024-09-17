# ABC-369 A - 369
# https://atcoder.jp/contests/abc369/tasks/abc369_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B = getIntMap()

    print(1 if A == B else 3 if abs(A - B) % 2 == 0 else 2)


if __name__ == "__main__":
    main()
