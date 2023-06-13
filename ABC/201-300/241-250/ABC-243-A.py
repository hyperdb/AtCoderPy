# ABC-243 A - Shampoo
# https://atcoder.jp/contests/abc243/tasks/abc243_a
#
def getIntMap():
    return map(int, input().split())

def main():
    v, a, b, c = getIntMap()

    v %= (a + b + c)

    print('F' if a > v else 'M' if a + b > v else 'T')

if __name__ == "__main__":
    main()