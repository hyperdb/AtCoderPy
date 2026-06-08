# ABC-460 A - Mod While Positive
# https://atcoder.jp/contests/abc460/tasks/abc460_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    count = 0
    while M > 0:
        _, m = divmod(N, M)
        count += 1
        M = m
    print(count)


if __name__ == "__main__":
    main()
