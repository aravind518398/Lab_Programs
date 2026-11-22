def find_frequency(string, char):
    return string.count(char)

def replace_char(string, old_char, new_char):
    return string.replace(old_char, new_char)

def remove_first_occurrence(string, char):
    return string.replace(char, '', 1)

def remove_all_occurrences(string, char):
    return string.replace(char, '')

while True:
    print("\n--Menu--")
    print("a. Find the frequency of a character in a string.")
    print("b. Replace a character by another character in a string.")
    print("c. Remove the first occurrence of a character from a string.")
    print("d. Remove all occurrences of a character from a string.")
    print("e. Exit")

    choice = input("\nEnter a choice a/b/c/d/e : ").lower()

    if choice == 'e':
        print("Exiting the program")
        break
    string = input("Enter a string: ")
    if choice == 'a':
        char = input("Enter the character to find frequency: ")
        print(f"Frequency of {char} in the string is: {find_frequency(string, char)}")
    elif choice == 'b':
        old_char = input("Enter the character to be replaced: ")
        new_char = input("Enter the new character: ")
        print(f"Modified string: {replace_char(string, old_char, new_char)}")
    elif choice == 'c':
        char = input("Enter the character to remove (first occurance): ")
        print(f"Modified string: {remove_first_occurrence(string, char)}")
    elif choice == 'd':
        char = input("Enter the character to remove (all occurrence): ")
        print(f"Modified string: {remove_all_occurrences(string, char)}")
    else:
        print("Invalid choice! Please select a valid option.")


  




