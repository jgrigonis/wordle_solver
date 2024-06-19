"""
Given a history and colorization, determine the words that can still
work, filtering out those that can't match.
"""

import wordle


guess_history = []
guess_history.append(wordle.Word("slate"))
for guess in guess_history:
    print(guess)
