#Square Every Digit

digit = '9119'
digit_to_str = ''
for i in digit:
    digit_to_str += str(int(i)* int(i))

print(digit_to_str)