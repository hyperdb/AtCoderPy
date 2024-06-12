# ABC-040 B - □□□□□
# https://atcoder.jp/contests/abc040/tasks/abc040_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    r = n
    for x in range(1, n + 1):
        y = n // x
        if x > y:
            break
        v = (y - x) + (n - x * y)
        r = min(r, v)
    print(r)


if __name__ == "__main__":
    main()
