# q5 Vowel & Consonant Counter

# input
word = input('Enter a word: ')

# processing
vowel = 0
consonant = 0

for character in word:
    if character in 'aeiouAEIOU':
        vowel += 1
    else:
        consonant += 1

# output
print('There are', vowel, 'vowels.')
print('There are', consonant, 'consonants.')
