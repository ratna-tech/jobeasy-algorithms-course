# Greatest Common divisor using recurssion
def common_divisor(num1,num2):
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2%num1
    if num1==0 or num2==0:
        print(num1 + num2)
    else: common_divisor(num1,num2)

num_1 = int(input(" Input any positive number  "))
num_2 = int(input(" Input any positive number  "))

common_divisor(num_1,num_2)