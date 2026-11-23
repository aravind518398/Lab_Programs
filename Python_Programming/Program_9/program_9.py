def select_even_values(t1):
    size = len(t1)
    t2 = []
    for i in range(0, size):
        if t1[i] % 2 == 0:
            t2.append(t1[i])
    return t2

def find_min_max(t1):
    minimum = min(t1)
    maximum = max(t1)
    return (minimum, maximum)
        
def split_tuple(t1):
    size = len(t1) - 1
    mid_value = (0+size)//2
    first_half = []
    second_half = []
    for i in range(0, mid_value+1):
        first_half.append(t1[i])
    for x in range(mid_value+1, size+1):
        second_half.append(t1[x])
    return tuple(first_half), tuple(second_half)

def concatenate_tuple(t1, t2):
    return t1 + t2



t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)
(first_half, second_half) = split_tuple(t1)
print("a. ")
print("\tFirst half: ",first_half)
print("\tSecond half: ",second_half) 
print("b. ")
print(f"\tt2 = {tuple(select_even_values(t1))}")
print("c. ")
print("\t",concatenate_tuple(t1, t2))

(min, max) = find_min_max(t1)
print("d.")
print(f"\tmin_value = {min}")
print(f"\tmax_value = {max}")
