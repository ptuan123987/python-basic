def main():
    text = "lua nep la lua nep lang lua len lop lop long nang lang lang"
    # word_count is dictionary (ordered , changeable and does not allow duplicates)
    # dictionary similar map in java
    word_count = {};
    for i in text.split(" ") : 
        word_count[i] = word_count.get(i,0) + 1;
    print(word_count);
main();
