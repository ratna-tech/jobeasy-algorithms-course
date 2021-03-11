#Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE
original_string= input('Enter any string ')
substr_to_replace = input('Enter substring to replace from original string ')
substr_to_replace_with = input('Enter substring that will replace other substring ')

i = (original_string.find(substr_to_replace))
sliced_string = original_string[0:i]  + substr_to_replace_with + original_string[i +len(substr_to_replace):]

print(sliced_string)