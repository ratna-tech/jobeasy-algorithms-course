#Disemvowel Trolls
#remove vowels from a string

original_str = "This website is for losers LOL!"
lowercase_str = original_str.lower()
vowel_str = 'aeiou'
new_str =''
for ch in lowercase_str:
    if ch not in vowel_str:
        new_str += ch

print(new_str)