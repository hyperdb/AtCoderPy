# ABC-120 B - K-th Common Divisor
# https://atcoder.jp/contests/abc120/tasks/abc120_b
#
def getIntMap():
    return map(int, input().split())


def div(n):

    if n == 1:
        return [1]

    a = []

    for i in range(1, n + 1):
        j = n // i

        if n % i == 0:
            a.append(i)
            a.append(j)

        if i >= j:
            break

    a = list(set(a))
    a.sort()

    return a


def main():
    a, b, k = getIntMap()

    x = div(a)
    y = div(b)
    z = []

    for i in x:
        if i in y:
            z.append(i)

    z.reverse()

    print(z[k - 1])


if __name__ == "__main__":
    main()
