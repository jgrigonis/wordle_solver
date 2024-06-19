"""
Look at every word in the guess_words.txt.

Score them based on the letter frequencies, then sort them

Seems like double letters should make the score lower.

"""

import os
import wordle
import data.letter_freqs

# print(data.letter_freqs.letter_frequencies)
# quit()

LOCAL_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
)

x = wordle.Wordle()
d = {}

for word in x.guess_words_list:
    value = 0
    for letter in set(word):
        value += data.letter_freqs.letter_frequencies.get(letter)
    d.update({word: value})


sd = dict(sorted(d.items(), key=lambda item: item[1]))
print(sd)
