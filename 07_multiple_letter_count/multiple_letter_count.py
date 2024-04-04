def multiple_letter_count(phrase):
    letterIndex = {}

    for ltr in phrase:
        letterIndex[ltr] = letterIndex.get(ltr, 0) +1

    return letterIndex




print(multiple_letter_count('yay'))

"{'y': 2, 'a': 1}"

print(multiple_letter_count('Yay'))

"{'Y': 1, 'a': 1, 'y': 1}"
