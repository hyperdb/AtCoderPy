# ABC-327 B - A^A
# https://atcoder.jp/contests/abc327/tasks/abc327_b
#
def getInt():
    return int(input())


def main():
    b = getInt()
    a = 0

    while True:
        a += 1
        aa = a ** a
        if aa == b:
            print(a)
            break
        elif aa > b:
            print(-1)
            break


if __name__ == "__main__":
    main()
