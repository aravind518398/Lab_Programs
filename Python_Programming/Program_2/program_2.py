
def find_power(m, n):
    return m**n


m = int(input("Enter the base (m): "))
n = int(input("Enter the exponent (n): "))

result = find_power(m, n)

print(f"{m}^{n} = {result}")