# ABC-200 B - 200th ABC-200
# https://atcoder.jp/contests/abc200/tasks/abc200_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, k = getIntMap()

    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = n * 1000 + 200
    print(n)


if __name__ == "__main__":
    main()
