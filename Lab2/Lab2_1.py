# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.

def reduce_adjacent_duplicates(nums):
    result = []

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            result.append(nums[i])

    return result

nums = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(reduce_adjacent_duplicates(nums)) 
