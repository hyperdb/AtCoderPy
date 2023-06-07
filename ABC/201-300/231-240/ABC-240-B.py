# ABC-240 B - Count Distinct Integers
# https://atcoder.jp/contests/abc240/tasks/abc240_b
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    a = getIntList()

    print(len(set(a)))

if __name__ == "__main__":
    main()