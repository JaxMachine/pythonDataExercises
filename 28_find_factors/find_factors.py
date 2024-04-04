def find_factors(num):

    number_list = [number for number in range (1, num // 2+1) if num % number == 0]

    number_list.append(num)

    return number_list


    """Find factors of num, in increasing order."""

print(find_factors(10))
"[1, 2, 5, 10]"

print(find_factors(11))
"[1, 11]"

print(find_factors(111))
"[1, 3, 37, 111]"

print(find_factors(321421))
"[1, 293, 1097, 321421]"
