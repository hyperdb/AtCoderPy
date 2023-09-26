#
#
#
def getString():
    return input()


def main():
    s = getString()

    print('Yes' if s in ['ACE', 'BDF', 'CEG', 'DFA', 'EGB', 'FAC', 'GBD'] else 'No')


if __name__ == "__main__":
    main()
