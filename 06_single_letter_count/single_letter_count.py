def single_letter_count(word, letter):
    return word.lower().count(letter.lower())


    """How many times does letter appear in word (case-insensitively)?"""
    
print(single_letter_count('Hello World', 'h'))

'1'
        
print(single_letter_count('Hello World', 'z'))
'0'
        
print(single_letter_count("Hello World", 'l'))

'3'

