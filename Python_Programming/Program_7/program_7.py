"""
Using Numpy module write menu driven program to do following

a. Create and array filled with 1's.
b. Find maximum and minimum values from an array
c. Dot product of 2 arrays.
d. Reshape a 1-D array to 2-D array.
"""


import numpy as np


def ones_array():
    shape = tuple(map(int, input("Enter the dimensions seperated by space (eg: 2 3 for 2x3): ").split()))
    print(f" Array filled with 1's:\n{np.ones(shape)}")

def find_min_max():
    arr = np.array(list(map(int, input("Enter the array elements: ").split())))
    print(f"Maximum value of array: {max(arr)}")
    print(f"Minimum value of array: {min(arr)}")

def dot_product():
    arr_one = np.array(list(map(int, input("Enter elements for array_one: ").split())))
    arr_two = np.array(list(map(int, input("Enter elements for array_two: ").split())))
    if arr_one.size != arr_two.size:
        print("Array must be of the same size for dot product.")
    else:
        print(f"Dot Product: {np.dot(arr_one, arr_two)}")

def reshape_array():
    arr = np.array(list(map(int, input("Enter array elements: ").split())))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    if rows * cols != arr.size:
        print("Cannot reshape array: total elements do not match.")
    else:
        reshaped = arr.reshape((rows, cols))
        print("Reshaped 2-D array: \n", reshaped)

while True:
    print("\t--Menu--")
    print("a. Create and array filled with 1's.")
    print("b. Find maximum and minimum values from an array")
    print("c. Dot product of 2 arrays.")
    print("d. Reshape a 1-D array to 2-D array.")
    print("e. Exit")
    choice = input("Enter your choice a/b/c/d/e: ").lower()

    if choice == 'e':
        print("Exiting program.")
        break

    if choice == 'a':
        ones_array()
    elif choice == 'b':
        find_min_max()
    elif choice == 'c':
        dot_product()
    elif choice == 'd':
        reshape_array()
        
        

        









