# ABC-076 B - Addition and Multiplication
# https://atcoder.jp/contests/abc076/tasks/abc076_b
#
def getInt():
    return int(input())


def main():
    n = getInt()
    k = getInt()

    r = 1
    for i in range(n):
        a = 2 * r
        b = r + k
        r = a if a <= b else b
    print(r)


if __name__ == "__main__":
    main()
