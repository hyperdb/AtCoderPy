# ABC-282 A - Generalized ABC
# https://atcoder.jp/contests/abc282/tasks/abc282_a
#
def getInt():
    return int(input())


def main():
    n = getInt()
    a = ord('A')

    s = ''
    for i in range(n):
        s += chr(a + i)
    print(s)


if __name__ == "__main__":
    main()
