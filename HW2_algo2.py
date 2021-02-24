#Zeros not for Heros
#print(countNumbers ending with zeros are boring. They might be
# fun in your world, but not here. Get rid of them. Only the ending ones.
#_num)
num = 9060

def remove_trail_0(num):
    num_n0_zer0 =0
    if num % 10 == 0:
      num_n0_zer0= num //10
      return num_n0_zer0
    else: return num

def check_trail_0(num):
    num_2 = remove_trail_0(num)
    #print(num_2)
    if num_2% 10 ==0:
        #print(num_2)
        check_trail_0(num_2)
        #print(num_2)
    else:print(num_2)

check_trail_0(num)
