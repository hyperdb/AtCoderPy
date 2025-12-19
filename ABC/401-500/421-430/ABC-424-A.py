# ABC-424 A - Isosceles
# https://atcoder.jp/contests/abc424/tasks/abc424_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    A = getIntList()

    print("No" if len(set(A)) == 3 else "Yes")


if __name__ == "__main__":
    main()
