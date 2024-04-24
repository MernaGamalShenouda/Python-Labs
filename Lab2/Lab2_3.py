# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

def are_all_unique(numbers):
    unique_numbers = set(numbers)
    
    if len(numbers) == len(unique_numbers):
        return True
    else:
        return False

sequence1 = [1, 5, 7, 9]
sequence2 = [2, 4, 5, 5, 7, 9]
print(are_all_unique(sequence1))  
print(are_all_unique(sequence2)) 
