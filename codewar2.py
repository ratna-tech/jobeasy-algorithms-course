#Create a method take that accepts a list/array and a number n,
# and returns a list/array array of the first n elements from the list/array.
num_list = [1,2,3,4,5]
n =3
def split_list(list,n):
    return(num_list[1:n])

new_list = split_list(num_list,n)
print(new_list)
