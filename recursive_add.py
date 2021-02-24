#Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.
number = int(input('enter any number  '))

def Recursive_add(num):
    num_1 = 0
    if num >9:
     num_1 = num_1 + num //10
     num_1 = num_1 + num % 10
     #print(num_1)
    if num_1 >9:
     Recursive_add(num_1)
    else: print(num_1)

Recursive_add(number)
