# ABC-218 B - qwerty
# https://atcoder.jp/contests/abc218/tasks/abc218_b
#
def getIntList():
    return list(map(int, input().split()))


def main():
    p = getIntList()

    a = ord('a') - 1
    s = []
    for i in p:
        s.append(chr(a + i))
    print(''.join(s))


if __name__ == "__main__":
    main()
