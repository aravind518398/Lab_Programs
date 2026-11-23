def find_all_occurance(main_string, sub_string):
    indices = []
    index = main_string.find(sub_string)
    while index != -1:
        indices.append(index)
        index = main_string.find(sub_string, index + 1)

    return indices if indices else -1

main_string = input("Enter the main string: ")
sub_string = input("Enter the sub string to search for: ")
indices = find_all_occurance(main_string, sub_string)
print(f"Indices: {indices}")