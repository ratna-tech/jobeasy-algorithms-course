#Enter a string of words separated by spaces. Find the longest word.
string = 'find the longest word in the string'
array_from_str = string.split()
length1=0
for word in array_from_str:
    length = len(word)
    if length > length1:
        length1 = length
        longest_word = word
print(longest_word)