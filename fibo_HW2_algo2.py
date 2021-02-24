# TODO: HW: Rewrite code, which will return only needed element of Fib sequence
# Program to return the Fibonacci number for a specific number using recursion
result = []
def fibbonacci(n):
    if n< 0:
        return "not valid"
    if n==0:
        return 0
    if n ==1:
        return[1]
    if n==2:
        return [1]
    index=3
    fib_1=1
    fib_2=1
    result = [1, 1]
    while index<= n:
      result.append(fib_1 + fib_2)
      fib_1,fib_2 = fib_2, fib_1+ fib_2
      index+=1
    return result[n-1]
element = int(input('enter a number '))
print(fibbonacci(element))