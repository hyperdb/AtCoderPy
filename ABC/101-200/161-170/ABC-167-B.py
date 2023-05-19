# ABC-167 B - Easy Linear Programming
# https://atcoder.jp/contests/abc167/tasks/abc167_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, k = getIntMap()

    s = 0
    if a >= k or a + b >= k:
        s = a if a <= k else k
    else:
        k -= (a + b)
        s = a - (c if c < k else k)
    print(s)


if __name__ == "__main__":
    main()
