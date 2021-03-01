#Digital root is the recursive sum of all the digits in a number.

number = int(input('enter any number  '))

def Recursive_digital_root(num):
    num_1 = 0
    if num >9:
     num_1 = num_1 + num //10
     num_1 = num_1 + num % 10
    if num_1 >9:
     Recursive_digital_root(num_1)
    else: print(num_1)

Recursive_digital_root(number)