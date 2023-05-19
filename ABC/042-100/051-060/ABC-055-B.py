# ABC-055 B - Training Camp
# https://atcoder.jp/contests/abc055/tasks/abc055_b
#
def getInt():
    return int(input())


def main():
    n = getInt()
    p = 10 ** 9 + 7

    r = 1
    for i in range(n):
        r = (r * (i + 1)) % p
    print(r)


if __name__ == "__main__":
    main()
