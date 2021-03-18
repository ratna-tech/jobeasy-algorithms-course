#Your task is to make a function that can take any non-negative integer as an argument and return it
# with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

digit = 1627384
digit_to_str= str(digit)

list=[]
str_highestnum = ''
def high_num(digit_to_str,list,str_highestnum):
 if digit_to_str ==0:
     return 0
 if len(digit_to_str)<2:
     return digit_to_str
 for i in digit_to_str:
    list.append(int(i))
 list.sort(reverse=True)
 for i in list:
    str_highestnum += str(i)
 #print(str_highestnum)
 return str_highestnum

print(high_num(digit_to_str,list,str_highestnum))