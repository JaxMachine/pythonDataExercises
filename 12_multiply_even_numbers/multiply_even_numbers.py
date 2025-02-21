def multiply_even_numbers(nums):

    output = 1

    for number in nums:
        if number % 2 == 0:
            output = output * number
    return output


    """Multiply the even numbers."""
    
print(multiply_even_numbers([2, 3, 4, 5, 6]))
"48"
        
print(multiply_even_numbers([3, 4, 5]))
"4"
        
        
"""If there are no even numbers, return 1."""

print(multiply_even_numbers([1, 3, 5]))
"1"
