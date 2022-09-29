def main():
    # use list ,map , filter
    numbers = list(map(int, input("Enter list number : ").split(" ")))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)
    square_numbers = list(
        map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    print(square_numbers)
    filter()


main()
