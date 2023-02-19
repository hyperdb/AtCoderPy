# ABC-136 B - Uneven Numbers
# https://atcoder.jp/contests/abc136/tasks/abc136_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    i = n
    c = 0
    while i > 0:
        if len(str(i)) % 2 == 1:
            c += 1
        i -= 1
    print(c)


if __name__ == "__main__":
    main()
