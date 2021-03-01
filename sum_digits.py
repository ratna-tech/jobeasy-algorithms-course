# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

num = int(input('input any whole num greater than 0'))
count = 0
count_num = num
#counting number of digits in number entered
while(count_num >0):
    count_num = count_num // 10
    count = count +1

added_num = 0
#adding digits after separating them
def add_num(num,count):
    global added_num
#separating digits from the whole num entered
    while count >0:
     count = count -1
     a=  num % 10
     added_num = added_num + a
     num = num // 10
    return (added_num)

final_num = add_num(num,count)
print(final_num)

