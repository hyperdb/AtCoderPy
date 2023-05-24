# ABC-231 A - Water Pressure
# https://note.nkmk.me/python-check-int-float/
#
def getInt():
    return int(input())


def main():
    x = getInt()

    m = x / 100

    print("%d" % m if m.is_integer() else m)


if __name__ == "__main__":
    main()
