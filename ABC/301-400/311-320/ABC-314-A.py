# ABC-314 A - 3.14
# https://atcoder.jp/contests/abc314/tasks/abc314_a
#
def getInt():
    return int(input())

def main():
    n = getInt()
    p = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679';

    print(p[:n+2])

if __name__ == "__main__":
    main()