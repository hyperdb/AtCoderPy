# ABC-393 A - Poisonous Oyster
# https://atcoder.jp/contests/abc393/tasks/abc393_a
#
def getStringMap():
    return input().split()


def main():
    taka, ao = getStringMap()

    r = 3
    if taka == "fine" and ao == "fine":
        r = 4
    elif taka == "sick" and ao == "sick":
        r = 1
    elif taka == "sick" and ao == "fine":
        r = 2

    print(r)


if __name__ == "__main__":
    main()
