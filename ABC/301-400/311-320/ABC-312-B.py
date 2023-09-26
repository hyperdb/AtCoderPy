# ABC-312 B - TaK Code
# https://atcoder.jp/contests/abc312/tasks/abc312_b
#

def getIntMap():
    return map(int, input().split())

def getStringRow(N):
    return [input() for _ in range(N)]

def chk(c):
    a = ['###.', '###.', '###.', '....', '....', '.###', '.###', '.###']
    t = [c[0][0:4], c[1][0:4], c[2][0:4], c[3][0:4], c[5][5:9], c[6][5:9], c[7][5:9], c[8][5:9]]

    return a == t

def main():
    n,m = getIntMap()
    s = getStringRow(n)

    for y in range(n - 9 + 1):
        for x in range(m - 9 + 1):
            r = []
            for i in range(9):
                r.append(s[y+i][x:x+9])
            if chk(r):
                print(y+1, x+1)

if __name__ == "__main__":
    main()