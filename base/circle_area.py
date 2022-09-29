
def main():
    first_number = float(input("First number : "))
    second_number = float(input("Second number : "))
    result = greatest_common_divisor(first_number, second_number)
    print(f"Result is {result}")


def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)


main()
