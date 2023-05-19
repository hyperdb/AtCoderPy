# ABC-156 B - Digits
# https://atcoder.jp/contests/abc156/tasks/abc156_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, k = getIntMap()

    c = 0
    while True:
        m = n % k
        c += 1

        n = n // k
        if n == 0:
            break

    print(c)


if __name__ == "__main__":
    main()
