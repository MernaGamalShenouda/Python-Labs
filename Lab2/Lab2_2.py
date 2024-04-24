# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)

def divide_strings(a, b):
    mid_a = (len(a) + 1) // 2
    mid_b = (len(b) + 1) // 2

    result = a[:mid_a] + b[:mid_b] + a[mid_a:] + b[mid_b:]

    return result

a = "abcdef"
b = "12345"
print(divide_strings(a, b))  
