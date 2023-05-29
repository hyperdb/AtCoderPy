# ABC-234 A - Weird Function
# https://atcoder.jp/contests/abc234/tasks/abc234_a
#
def getInt():
    return int(input())

def fx(n):
    return n ** 2 + 2 * n + 3

def main():
    t = getInt()

    print(fx(fx(fx(t) + t) + fx(fx(t))))


if __name__ == "__main__":
    main()