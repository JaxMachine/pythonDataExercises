def reverse_vowels(s):

    vowels = set("aeiou")

    output_string = list(s)

    i= 0
    j = len(s) - 1

    while i < j:
        if output_string[i].lower() not in vowels:
            i += 1
        elif output_string[j].lower() not in vowels:
            j -= 1
        else:
            output_string[i], output_string[j] = output_string[j], output_string[i]
            i +=1
            j -= 1
    
    return "".join(output_string)

"""Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order."""

print(reverse_vowels("Hello!"))
'Holle!'

print(reverse_vowels("Tomatoes"))
'Temotaos'

print(reverse_vowels("Reverse Vowels In A String"))
'RivArsI Vewols en e Streng'

print(reverse_vowels("aeiou"))
'uoiea'

print(reverse_vowels("why try, shy fly?"))
'why try, shy fly?'