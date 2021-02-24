#You get an array of numbers, return the sum of all of the positives ones.
k = int(input("Enter size of array:"))
array_1 =[]
for i in range(0, k):
    num = int(input("Enter an array element:" ))
    array_1.append(num)

def add_pos(array_1):
    add_posnum = 0
    for items in array_1:
        if items > 0:
            add_posnum = add_posnum + items
    print(add_posnum)

add_pos(array_1)
