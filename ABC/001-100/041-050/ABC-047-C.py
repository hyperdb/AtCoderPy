#
#
#
def getString():
    return input()


def main():
    S = getString()

    print(S.count("WB") + S.count("BW"))


if __name__ == "__main__":
    main()
