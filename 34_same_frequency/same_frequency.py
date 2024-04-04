def same_frequency(num1, num2):

    count_number_1 = {}
    count_number_2 = {}

    for x in (str(num1)):
        count_number_1[x] = count_number_1.get(x, 0) + 1
    
    for y in (str(num2)):
        count_number_2[y] = count_number_2.get(y, 0)+ 1
    
    return count_number_1 == count_number_2


    "Do these nums have same frequencies of digits?"
    
print(same_frequency(551122, 221515))
"True"
        
print(same_frequency(321142, 3212215))
"False"
        
print(same_frequency(1212, 2211))
"True"