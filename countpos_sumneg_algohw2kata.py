#Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers.
k = int(input("Enter size of array:"))
array_1 =[]
for i in range(0, k):
    num = int(input("Enter an array element:" ))
    array_1.append(num)

def sum_neg_addpos(array_1):
    add_negnum = 0
    count = 0
    for items in array_1:
        if items < 0:
         add_negnum = add_negnum + items
        else: count += 1
    array_2 =[count,add_negnum]
    return(array_2)

final_array= sum_neg_addpos(array_1)
print(final_array)