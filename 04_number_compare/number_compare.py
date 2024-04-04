def number_compare(a, b):

    if a == b :
        return "Numbers are equal"
    
    if a > b:
        return "First Is greater"

    if b> a :
        return "Second is greater"
    


    
print(number_compare(1, 1))

'Numbers are equal'
        
print(number_compare(-1, 1))

'Second is greater'
        
print(number_compare(1, -2))

'First is greater'

