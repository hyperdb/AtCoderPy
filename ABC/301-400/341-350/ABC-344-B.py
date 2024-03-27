# ABC-344 B - Delimiter
# https://atcoder.jp/contests/abc344/tasks/abc344_b
#
def getInt():
    return int(input())


def main():

    a = []
    while True:
        n = getInt()
        a.append(n)
        if n == 0:
            break

    a.reverse()
    for i in a:
        print(i)


if __name__ == "__main__":
    main()
