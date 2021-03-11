#Return the number (count) of vowels in the given string.

vowel_string = 'aeiou'
check_str = input('input any character string all lower case')

def count_vowel(check_str, vowel_string):
 count = 0
 for ch in check_str:
    if ch in vowel_string:
       count +=1
 return count

print(count_vowel(check_str,vowel_string))