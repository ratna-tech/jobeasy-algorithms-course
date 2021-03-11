#Enter an irregular string (that means it may have space at the beginning of a string,
# at the end of the string, and words may be separated by several spaces).
# Make the string regular (delete all spaces at the beginning and end of the string,
# leave one space separating words).

original_str = "   irregular    string  convert    in   to      regular   str   "
removespace = original_str.split()
str =''
def regular_str(string):
 global str
 for ch in string:
    str += ch
    str +=' '
 return str

print(regular_str(removespace))
