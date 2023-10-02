# ABC-317 A - Potions
# https://atcoder.jp/contests/abc317/tasks/abc317_a
#
def getIntMap():
    return map(int, input().split())

def getIntList():
    return list(map(int, input().split()))

def main():
    n, h, x = getIntMap()
    a = [0] + getIntList()
    b = [i for i in range(len(a)) if a[i] >= x - h]

    print(min(b))

if __name__ == "__main__":
    main()