#When given a list, the program should return a list of all the elements that are below the arithmetical
# mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

list = list1 = ['a', '1', 1, 2.5, "male"]
add_list = 0
mean = 0
def find_mean(list):
 global add_list
 global mean
 for i in list:
    if type(i)==int or type(i)==float:
        add_list += i
 if add_list >0:
  mean = ((add_list / len(list)))
 return mean

mean_of_list = find_mean(list1)
if mean_of_list>0:
    print(mean_of_list/len(list))
else:print("List is not made of numbers")

