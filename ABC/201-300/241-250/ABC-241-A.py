# ABC-241 A - Digit Machine
# https://atcoder.jp/contests/abc241/tasks/abc241_a
#
def getIntList():
    return list(map(int, input().split()))

def main():
    a = getIntList()

    n = 0
    for i in range(3):
        n = a[n]
    print(n)

if __name__ == "__main__":
    main()