# ABC-336 C - Even Digits
# https://atcoder.jp/contests/abc336/tasks/abc336_c
#
def getInt():
    return int(input())


def main():
    n = getInt()
    s = ['0', '2', '4', '6', '8']

    a = n - 1
    b = []
    while True:
        d, m = divmod(a, 5)
        b.append(m)
        if d < 5:
            if d > 0:
                b.append(d)
            break
        else:
            a = d
    c = [s[x] for x in b]
    c.reverse()

    print("".join(c))


if __name__ == "__main__":
    main()