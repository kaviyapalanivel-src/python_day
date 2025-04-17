def filter_even_numbers(numbers):
    # Use filter with a lambda function to filter even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original Numbers:", numbers)
    print("Even Numbers:", filter_even_numbers(numbers))

main()
