def main():
    aList = list(input("Enter text : ").split(" "))
    print(aList)

    print(most_common(aList))
    print("hello world")


def most_common(list):
    counter = 0
    word_common = list[0]
    for i in list:
        cur_frequency = list.count(i)
        if (cur_frequency > counter):
            counter = cur_frequency
            word_common = i
    return word_common



main()
