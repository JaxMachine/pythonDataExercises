def is_odd_string(word):
    DIFF = ord("a") - 1

    output = sum((ord(character) - DIFF) for character in word.lower())
    return output % 2 == 1

    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:"""
    
print(is_odd_string('a'))
"True"

print(is_odd_string('A'))
"True"

"These sum to 4, which is not odd:"
    
print(is_odd_string('aaaa'))
"False"

print(is_odd_string('AAaa'))
"False"

"""Longer example:"""
    
print(is_odd_string('amazing'))
"True"

    # Hint: you may find the ord() function useful here