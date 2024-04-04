def flip_case(phrase, to_swap):

    to_swap = to_swap.lower()
    output =""

    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
        output += letter
    return output

    """Flip [to_swap] case each time it appears in phrase."""

print(flip_case('Aaaahhh', 'a'))
'aAAAhhh'

print(flip_case('Aaaahhh', 'A'))
'aAAAhhh'

print(flip_case('Aaaahhh', 'h'))
'AaaaHHH'

