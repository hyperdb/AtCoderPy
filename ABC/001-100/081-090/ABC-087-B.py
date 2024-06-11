# ABC-087 B - Coins
# https://atcoder.jp/contests/abc087/tasks/abc087_b
#
def getInt():
    return int(input())


def main():
    a = getInt()
    b = getInt()
    c = getInt()
    x = getInt()

    a = a if x // 500 >= a else x // 500
    b = b if x // 100 >= b else x // 100
    c = c if x // 50 >= c else x // 50

    r = 0

    for i in range(a + 1):
        for j in range(b + 1):
            if (i * 500) + (j * 100) > x:
                break

            for k in range(c + 1):
                s = (i * 500) + (j * 100) + (k * 50)
                if s > x:
                    break
                if s == x:
                    r += 1
    print(r)


if __name__ == "__main__":
    main()
