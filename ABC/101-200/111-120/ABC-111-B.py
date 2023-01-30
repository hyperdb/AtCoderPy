# ABC-111 B - AtCoder Beginner Contest 111
# https://atcoder.jp/contests/abc111/tasks/abc111_b
#
def getInt():
    return int(input())


def ns(n):
    return n * 100 + n * 10 + n


def main():
    n = getInt()

    a = 0
    for i in range(9):
        m = ns(9 - i)
        if n <= m:
            a = m
            continue
        else:
            break
    print(a)


if __name__ == "__main__":
    main()
