#Given an array of integers your solution should find the smallest integer.
original_array = [4,7,9,1,23,-7,-1,0]
small_num = original_array[0]
for i in range(1, len(original_array)):
    if original_array[i] < small_num:
        small_num = original_array[i]
print(small_num)