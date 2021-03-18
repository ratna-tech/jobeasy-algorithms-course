#When given a list of elements find the two lowest elements. They can be equal to each other or different.
original_list=[]
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    element = int(input("Enter elements: "))
    original_list.append(element)

original_list.sort()
print(original_list[0], original_list[1] )