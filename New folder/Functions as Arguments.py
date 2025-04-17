def custom_sort(lst, key_func):
    return sorted(lst, key=key_func)

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = custom_sort(numbers, key=lambda x: -x)  # Sort in descending order
print(sorted_numbers)