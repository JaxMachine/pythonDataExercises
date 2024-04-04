def triple_and_filter(nums):
    return [number * 3 for number in nums if number % 4 == 0]
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3."""
    
print(triple_and_filter([1, 2, 3, 4]))
"[12]"
        
print(triple_and_filter([6, 8, 10, 12]))
"[24, 36]"
        
print(triple_and_filter([1, 2]))
"[]"
