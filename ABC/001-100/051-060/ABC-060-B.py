# ABC-060 B - Choose Integers
# https://atcoder.jp/contests/abc060/tasks/abc060_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    f = False
    for i in range(b):
        if a * i % b == c:
            f = True
            break
    print('YES' if f else 'NO')


if __name__ == "__main__":
    main()
