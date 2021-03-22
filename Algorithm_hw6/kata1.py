#Mumbling
original_str = "abcdef"
len = len(original_str)
print(len)

def mult_char(original_str,len):
 newstr = ''
 for i in range(len):
    newstr+= original_str[i]*(i+1)
 return newstr


print(mult_char(original_str,len))