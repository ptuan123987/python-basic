def main():
    # map(function , input)
    aList = list(map(int, input("Enter number list : ").split(' ')))
    print(aList)
    aList.sort()
    print(aList)
    aList.sort(key=None, reverse=True)
    print(aList)
    aList.sort(key=lambda x: x * (x % 2), reverse=False)
    print(aList)


main()
