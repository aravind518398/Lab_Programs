def read_unique_integers():
    try:
        numbers = list(map(int,input("Enter a list of numbers sperated by spaces: ").split()))
        print(numbers)
        unique_integer = []
        for num in numbers:
            if num in unique_integer:
                raise ValueError(f"Duplicate value found: {num}")
            unique_integer.append(num)
        else:
            print("All numbers are unique.")
        
    except ValueError as e:
        print(f"Error: {e}")

read_unique_integers()