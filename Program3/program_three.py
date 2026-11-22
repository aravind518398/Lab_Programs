import matplotlib.pyplot as plt

ages = [
    23, 45, 34, 56, 67, 12, 78, 43, 21, 39, 50, 27,
    35, 62, 18, 64, 70, 30, 42, 15, 33, 54, 36, 25, 47, 60,
    21, 59, 22, 31, 40, 59, 52, 26, 61, 35, 48, 14, 68, 49, 19,
    27, 24, 55, 38, 53, 29, 57, 32, 24, 63, 41, 28, 66, 20, 37,
    48, 66, 51, 46, 62, 16, 13, 44, 65, 17, 75, 58, 30, 28, 23,
    26, 52, 33, 49, 56, 31, 54, 22, 43, 38, 40, 51, 47, 25,
    19, 63, 58, 29, 41, 15, 34, 55, 37, 60, 42, 20, 36,
    18, 39
]



plt.figure(figsize=(12,8))
plt.hist(ages, bins=10, facecolor="red", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age distribution in panchayath ward".title())
plt.show()