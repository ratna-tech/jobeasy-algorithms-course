#Write a Python function, which will count how many times a character (substring)
# is included in a string. DON’T USE METHOD COUNT

original_str = 'apple banana apple mango apple'
str_to_list = original_str.split()
sub ='apple'
def count_substr(string,sub):
    count = 0
    for ch in string:
        if sub == ch:
            count+=1
    return count
print(count_substr(str_to_list, sub))