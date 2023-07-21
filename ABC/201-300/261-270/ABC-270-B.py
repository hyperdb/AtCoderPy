# ABC-270 B - Hammer
# https://atcoder.jp/contests/abc270/tasks/abc270_b
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y, z = getIntMap()

    if x < 0:
        x *= -1
        y *= -1
        z *= -1

    # 0 x y z
    if x < y < z:
        print(x)
        exit
    # 0 x z y
    elif x < z < y:
        print(x)
        exit
    elif y < x < z:
        # y 0 x z
        if y < 0:
            print(x)
            exit
        # 0 y x z
        else:
            print(-1)
            exit
    elif y < z < x:
        # y 0 z x
        if y < 0:
            print(x)
            exit
        # 0 y z x
        else:
            print(-1)
            exit
    # (z) 0 z x y
    elif z < x < y:
        print(x)
        exit
    elif z < y < x:
        # z y 0 x
        if y < 0:
            print(x)
            exit
        else:
            # 0 z y x
            if z > 0:
                print(x)
                exit
            # z 0 y x
            else:
                print(x - 2 * z)
                exit


if __name__ == "__main__":
    main()
