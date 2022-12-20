# ABC-051 B - Sum of Three Integers
# https://atcoder.jp/contests/abc051/tasks/abc051_b
#
def getIntMap():
    return map(int, input().split())


def main():
    k, s = getIntMap()

    c = 0
    for x in range(k + 1):
        for y in range(k + 1):
            z = s - (x + y)
            if z >= 0 and z <= k:
                c += 1
    print(c)


if __name__ == "__main__":
    main()
