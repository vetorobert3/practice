"""
Find the first non-repeating character in a string of lowercase letters. Non-repeating is defined as a character that only appears once in a string. If all characters repeat, return an underscore.
"""

def first_not_repeating_character(s):
    letters = {}

    for i in s:
        if letters.get(i):
            letters[i] += 1
        else:
            letters[i] = 1

    for i in s:
        if letters[i] == 1:
            return i

    return "_"


letters = ("sskknnmbmq")
print(first_not_repeating_character(letters))