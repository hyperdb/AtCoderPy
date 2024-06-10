# 042 C - こだわり者いろはちゃん
# https://atcoder.jp/contests/abc042/tasks/arc058_a
#
def getIntList():
    return list(map(int, input().split()))


def getIntMap():
    return map(int, input().split())


def check_num(data, err_data):
    for n in set(list(map(int, list(str(data))))):
        if n in err_data:
            return False
    return True


def main():
    N, K = getIntMap()
    D = getIntList()

    for c in range(N, 100000):
        if check_num(c, D):
            print(c)
            break


if __name__ == "__main__":
    main()
