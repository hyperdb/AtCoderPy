# ABC-235 B - Climbing Takahashi
# https://atcoder.jp/contests/abc235/tasks/abc235_b
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    h = getIntList()

    x = 0
    for i in range(n):
        x = max(x, h[i])
        if i + 1 < n and h[i] >= h[i + 1]:
            break
    print(x)

if __name__ == "__main__":
    main()