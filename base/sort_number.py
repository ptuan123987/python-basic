

def main():
    aList = list(map(int, input("Enter number list : ").split(' ')))

    print(aList)
    # sort from largest number to smallest number
    aList.sort(reverse=True)
    print(aList)
    # sort from smallest number to largest number
    aList.sort(reverse=False)
    print(aList)
    # sort from even to odd
    aList.sort(key=keySort, reverse=None)
    print(aList)
    # sort from odd to even
    aList.sort(key=keySort, reverse=True)


def keySort(element):
    return element*(element % 2)


main()
