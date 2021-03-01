# Program to find the Fibonacci number  using recursion
result = [1, 1]
fib_1 = 1
fib_2 = 1
def fibbonacci(n):
    result = calc_fibonum(n)
    if len(result)< n:
        fibbonacci(n)
    return result

def calc_fibonum(n):
    global fib_2
    global fib_1
    if n< 0:
        return "not valid"
    if n==0:
        return 0
    if n ==1:
        return[1]
    if n==2:
        return [1,1]

    if n>=3:
     result.append(fib_1 + fib_2)
     fib_1, fib_2 = fib_2, fib_1 + fib_2

    return result
element = int(input('enter a number '))
print(fibbonacci(element))