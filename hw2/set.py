def main():
    first_numbers = list(
        map(int, input("Enter first numbers list : ").split(" ")))
    second_numbers = list(
        map(int, input("Enter second numbers list ").split(" ")))
    set_a = set(first_numbers)
    set_b = set(second_numbers)
    # different two sets
    print(set_a.difference(set_b))
    # intersection
    print(set_a.intersection(set_b))
    # union two sets
    print(set_a.union(set_b))


main()
