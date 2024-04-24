# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

num_rows = 5

for i in range(1, num_rows * 2):
    if i <= num_rows:
        print("* " * i)
    else:
        print("* " * (num_rows * 2 - i))
