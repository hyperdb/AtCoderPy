# ABC-432 A - Permute to Maximize
# https://atcoder.jp/contests/abc432/tasks/abc432_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    N = getIntList()

    N.sort()
    N.reverse()

    print("".join(map(str, N)))


if __name__ == "__main__":
    main()
