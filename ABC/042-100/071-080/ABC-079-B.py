# ABC-079 B - Lucas Number
# https://atcoder.jp/contests/abc079/tasks/abc079_b
#
def getInt():
    return int(input())


def main():
    n = getInt()
    l = [0] * (n + 1)

    l[0] = 2
    l[1] = 1
    for i in range(2, n + 1):
        l[i] = l[i - 1] + l[i - 2]
    print(l[n])


if __name__ == "__main__":
    main()
