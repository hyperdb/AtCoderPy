# ABC-378 A - Pairing
# https://atcoder.jp/contests/abc378/tasks/abc378_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    A = getIntList()

    c = 0
    for x in set(A):
        c += A.count(x) // 2
    print(c)


if __name__ == "__main__":
    main()
