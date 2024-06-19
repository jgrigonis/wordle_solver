"""
Look at all the answer words and guess words, and create some letter
frequency data. This should help in scoring possible guesses.

Used this script to create the letter_freqs.py
"""
# import os
import wordle


# LOCAL_DATA_DIR = os.path.join(
#     os.path.dirname(os.path.realpath(__file__)),
#     "data",
# )

x = wordle.Wordle()
d = {}

for word in x.answer_words_list:
    for letter in word:
        d[letter] = d.get(letter,0)+1
print(d)
#print(x.answer_words_list)
sd = dict(sorted(d.items(), key=lambda item: item[1]))
print(sd)
