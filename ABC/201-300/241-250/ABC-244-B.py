# ABC-244 B - Go Straight and Turn Right
# https://atcoder.jp/contests/abc244/tasks/abc244_b
#
def getInt():
    return int(input())

def getString():
    return input()

def move(dir, pos=[0,0]):
    if dir == 'E':
        pos[0] += 1
    elif dir == 'S':
        pos[1] -= 1
    elif dir == 'W':
        pos[0] -= 1
    elif dir == 'N':
        pos[1] += 1

    return pos

def main():
    n = getInt()
    s = list(getString())
    d = ['E', 'S', 'W', 'N']
    p = [0, 0]

    i = 0
    for c in s:
        if c == 'R':
            i = (i + 1) % 4
        else:
            p = move(d[i], p)

    print(p[0], p[1])

if __name__ == "__main__":
    main()