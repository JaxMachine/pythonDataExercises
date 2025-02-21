def sum_range(nums, start=0, end=None):

    if end is None:
        end = len(nums)
    return sum(nums[start:end + 1])


    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)"""

nums = [1, 2, 3, 4]

print(sum_range(nums))
"10"

print(sum_range(nums, 1))
"9"

print(sum_range(nums, end=2))
"6"

print(sum_range(nums, 1, 3))
"9"

"If end is after end of list, just go to end of list:"

print(sum_range(nums, 1, 99))
"9"
