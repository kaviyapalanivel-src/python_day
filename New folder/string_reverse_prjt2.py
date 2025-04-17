def reverse_string(s):
    reversed_s = ""
    for char in s:  # Intentional bug: Should be reversed_s += char instead of reversed_s = char
        reversed_s = char + reversed_s
    return reversed_s

def main():
    user_input = input("Enter a string: ")
    print("Reversed String:", reverse_string(user_input))  # Debug this line

main()
