def main():
    aList = list(input("Enter text : ").split(" "));
    word_count = {}
    for i in aList:
        word_count[i] =word_count.get(i,0) + 1;
    print(word_count);
main();