#program to find perfect number
def divisors(num):
    result = []
    for i in range(1,num+1):
        if num % i ==0:
            result.append(i)
    return result

def check_perfect_num(n):
    add_list_num = 0
    list =divisors(n)
    list_tocheck_pernum = list[:-1]
    print(list_tocheck_pernum)
    for i in list_tocheck_pernum:
        add_list_num = add_list_num + i
    if add_list_num == n:
        return "perfect number"
    else:
        return "not perfect number"

number_to_check = int(input("enter a positive num  "))
print(f'{number_to_check} is a',check_perfect_num(number_to_check))