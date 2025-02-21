def find_the_duplicate(nums):
    duplicates = set()

    for number in nums:
        if number in duplicates:
            return duplicates
        duplicates.add(number)

"""Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None"""

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
"1"

print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
"9"

print(find_the_duplicate([2, 1, 3, 4]) is None)
"True"
