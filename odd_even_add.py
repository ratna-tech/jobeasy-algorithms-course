#Count odd and even numbers
num = int(input('input any whole num greater than 0'))
count = 0
count_num = num
#counting number of digits in number entered
while(count_num >0):
    count_num = count_num // 10
    count = count +1
print("\n Number of Digits in a Given Number = %d" %count)
odd_num = 0
even_num = 0
check_even = 0
def add_num(num,count):
    global odd_num
    global even_num
#separating digits from the whole num entered
    while count >0:
     count = count -1
     a=  num % 10
     num = num // 10
# checking if num is even or odd
     if (a % 2) == 0:
          even_num += 1
     else:
         odd_num+= 1
    return(odd_num,even_num)
o,e = add_num(num,count)
print(o)
print(e)