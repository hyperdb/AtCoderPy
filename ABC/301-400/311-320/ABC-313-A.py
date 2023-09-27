# ABC-313 A - To Be Saikyo
# https://atcoder.jp/contests/abc313/tasks/abc313_a
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    a = getIntList()

    if n == 1:
        print(0)
    else:
        m = max(a[1:])
        print(0 if a[0] > m else 1 if a[0] == m else m - a[0] + 1)


if __name__ == "__main__":
    main()