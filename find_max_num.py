#Find max number from 3 values, entered manually from a keyboard
a = int(input('input any whole num greater than 0'))
b= int(input('input any whole num greater than 0'))
c= int(input('input any whole num greater than 0'))

def find_max(a,b,c):
    global max_num
    if a > b:
        max_num = a
    else: max_num = b
    if max_num > c:
        return(max_num)
    else:return(c)
Max_num = find_max(a,b,c)
print(Max_num)

