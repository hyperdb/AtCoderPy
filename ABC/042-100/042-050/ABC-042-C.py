# 042 C - こだわり者いろはちゃん
# https://atcoder.jp/contests/abc042/tasks/arc058_a
#
def getIntList():
    return list(map(int, input().split()))


def check_num(data, err_data):
    for n in set(list(map(int, list(str(data))))):
        if (n in err_data):
            return False
    return True


def main():
    param = getIntList()
    data = getIntList()

    for c in range(param[0], 10000):
        if (check_num(c, data)):
            print(c)
            break
    print(0)


if __name__ == "__main__":
    main()
