def even_or_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if even_or_odd(n):
    print(f"{n} is even")
else:
    print(f"{n} is odd")