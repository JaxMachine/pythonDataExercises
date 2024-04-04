def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None 
    return phrase * num

    """Return phrase, repeated num times."""

print(repeat('*', 3))
'***'

print(repeat('abc', 2))
'abcabc'

print(repeat('abc', 0))
''

"""Ignore illegal values of num and return None:"""

print(repeat('abc', -1) is None)
"True"

print(repeat('abc', 'nope') is None)
"True"
