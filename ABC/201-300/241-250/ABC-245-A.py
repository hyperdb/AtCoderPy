# ABC-245 A - Good morning
# https://atcoder.jp/contests/abc245/tasks/abc245_a
#
def getIntMap():
    return map(int, input().split())

def m(x, y):
    return x * 60 + y

def main():
    a, b, c, d = getIntMap()

    print('Takahashi' if m(a, b) <= m(c, d) else 'Aoki')

if __name__ == "__main__":
    main()