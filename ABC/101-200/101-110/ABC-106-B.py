# ABC-106 B - 105
# https://atcoder.jp/contests/abc106/tasks/abc106_b
#
def getInt():
    return int(input())


def countDiv(n):
    a = []
    for i in range(1, n + 1):
        if i > n // i:
            break

        if n % i == 0:
            a.append(i)
            a.append(n // i)

    return len(set(a))


def main():
    n = getInt()

    r = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        if countDiv(i) == 8:
            r += 1
    print(r)


if __name__ == "__main__":
    main()
