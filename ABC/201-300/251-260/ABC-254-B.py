# ABC-254 B - Practical Computing
# https://atcoder.jp/contests/abc254/tasks/abc254_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    r = []
    for j in range(n):
        c = []
        for i in range(j + 1):
            if 0 < i < j:
                c.append(r[j - 1][i - 1] + r[j - 1][i])
            else:
                c.append(1)
        r.append(c)

        print(" ".join(list(map(str, c))))


if __name__ == "__main__":
    main()
