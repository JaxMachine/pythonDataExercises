def mode(nums):

    frequency_count = {}

    for number in nums:
        frequency_count[number] = frequency_count.get(number, 0) + 1

    max_value = max(frequency_count.values())

    for (number, frequency) in frequency_count.items():
        if frequency == max_value:
            return number

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times."""

print(mode([1, 2, 1]))
"1"

print(mode([2, 2, 3, 3, 2]))
"2"
