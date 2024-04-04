def valid_parentheses(parens):

    parentheses_count = 0

    for paren in parens:
        if paren == '(':
            parentheses_count += 1
        elif paren == ')':
            parentheses_count -= 1
        if parentheses_count < 0 :
            return False
    
    return parentheses_count == 0

"""Are the parentheses validly balanced?"""
print(valid_parentheses("()"))
"True"

print(valid_parentheses("()()"))
"True"

print(valid_parentheses("(()())"))
"True"

print(valid_parentheses(")()"))
"False"

print(valid_parentheses("())"))
"False"

print(valid_parentheses("((())"))
"False"

print(valid_parentheses(")()("))
"False"