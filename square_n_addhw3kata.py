#Complete the square sum function so that it squares each number passed into it and then sums
# the results together.
original_list= [1,2,3,5,7,]
square_add =0
def square_n_sum(list):
    global square_add
    for i in list:
        square_add = square_add +i**2
    return square_add

print(square_n_sum(original_list))