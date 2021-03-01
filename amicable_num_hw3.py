#Amicable numbers
divisors= 0
divisors1 = 0
divisors2 = 0
divisorstemp =0
def get_divisors(num):
    global divisors
    global divisorstemp
    for i in range(1, num):
        if num%i ==0:

            divisorstemp= divisorstemp + i
    divisors = divisorstemp
    divisorstemp = 0
    return divisors


def find_amicable_num(num1,num2):
    divisors1 = get_divisors(num1)
    print(divisors1)
    divisors2 = get_divisors(num2)
    print(divisors2)
    if divisors1 == num2 and divisors2 == num1:
        print( f'{num1} and {num2} are amicable numbers')
    else: print(" {num1} and {num2} are not amicable numbers")

find_amicable_num(220,284)

