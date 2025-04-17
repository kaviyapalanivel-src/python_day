def string_tool():
    user_string = input("Enter a string: ")
    print("1. Reverse String")
    print("2. Change Case")
    print("3. Count Vowels")
    choice = input("Choose an option: ")
    
    if choice == '1':
        print(user_string[::-1])
    elif choice == '2':
        print(user_string.swapcase())
    elif choice == '3':
        vowels = "aeiouAEIOU"
        count = sum(1 for char in user_string if char in vowels)
        print(f"Number of vowels: {count}")

string_tool()