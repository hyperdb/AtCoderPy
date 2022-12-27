# ABC-058 A - ι⊥l
# https://atcoder.jp/contests/abc058/tasks/abc058_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()
    print('YES' if a + b + c == 3 * b else 'NO')


if __name__ == "__main__":
    main()
