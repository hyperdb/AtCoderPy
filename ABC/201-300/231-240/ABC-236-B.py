# ABC-236 B - Who is missing?
# https://atcoder.jp/contests/abc236/tasks/abc236_b
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    a = getIntList()

    b = {}
    for x in a:
        b.setdefault(x, 0)
        b[x] += 1

    r = [k for k, v in b.items() if v == 3]

    print(r[0])

if __name__ == "__main__":
    main()