#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.

str_words = 'String will never be empty and you do not need to account for different data types'
list_words = str_words.split()
print(list_words)
min_word = list_words[0]
def find_min_word(list_words,min_word):
 for ch in list_words:
    if len(ch) < len(min_word):
        min_word = ch
 return (len(min_word))
print(find_min_word(list_words,min_word))