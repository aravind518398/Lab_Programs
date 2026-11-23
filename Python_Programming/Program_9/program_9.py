
t1 = (1,2,5,7,9,2,4,6,8,10)

print("\na.Print contents of t1 in 2 separate lines such that half values come on one line an other half in the next line.")
half = len(t1) // 2
print(f"First half of t1: {t1[half : ]}")
print(f"Second half of t1: {t1[ : half]}")

print("\nb.Print all even values of t1 as antoher tuple t2.")
t2 = tuple(x for x in t1 if x % 2 == 0)
print(f"Tuples of even value (t2): {t2}")

print("\nc.Concatenate a tuple t2 = (11, 13, 15 with t1.)")
t2 = (11, 13, 15)
print(f"Concatenated tuple (t1 + t2): {t1 + t2}")

print("\nd.Return max and min from t1.")
print(f"Maximum value from t1: {max(t1)}")
print(f"Minimum value from t1: {min(t1)}")
