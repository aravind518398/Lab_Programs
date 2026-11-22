n = int(input("Enter the number of terms (n): "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total - i
    else:
        total = total + i

print(f"Sum of the series up to {n} terms is {total}")