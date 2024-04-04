def is_palindrome(phrase):
    phrase = phrase.lower().replace(' ', '')

    return phrase == phrase[::-1]

    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards)."""

print(is_palindrome('tacocat'))
"True"

print(is_palindrome('noon'))
"True"

print(is_palindrome('robert'))
"False"

"""Should ignore capitalization/spaces when deciding:"""

print(is_palindrome('taco cat'))
"True"

print(is_palindrome('Noon'))
"True"
