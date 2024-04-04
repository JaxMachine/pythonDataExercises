VOWELS = set("aeiou")

def vowel_count(phrase):

    phrase = phrase.lower()
    letter_counter = {}

    for letter in phrase:
        if letter in VOWELS:
            letter_counter[letter] = letter_counter.get(letter, 0)+1
    return letter_counter

    """Return frequency map of vowels, case-insensitive."""

print(vowel_count('rithm school'))
"{'i': 1, 'o': 2}"
        
print(vowel_count('HOW ARE YOU? i am great!') )
"{'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}"
