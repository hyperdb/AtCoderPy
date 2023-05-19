# ABC-116 B - Collatz Problem
# https://atcoder.jp/contests/abc116/tasks/abc116_b
#
def getInt():
    return int(input())


def calc(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def main():
    s = getInt()

    a = [s]
    i = 1
    while True:
        x = calc(a[i - 1])
        if x in a:
            print(i + 1)
            break
        i += 1
        a.append(x)


if __name__ == "__main__":
    main()
