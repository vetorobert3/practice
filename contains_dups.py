"""
Understand:
    Input: [1,2,3,1]
    output: true

    input: [1,2,3,4]
    output: false

    input: [1,1,1,3,3,4,3,2,4,2]
    output: true

Plan:
    if I remember correctly, I have to compare the array to
    to duplicate array that is made using the set(). set()
    will make a copy of the array only using the unique values
    meanig that it will only copy the values once even though 
    they appear more than once. Then if they equal, return false
    else return true meaning that they are not equal.
"""

def containsDuplicates(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True

test_1 = [1,2,3,1]
test_2 = [1,2,3,4]
test_3= [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicates(test_1))
print(containsDuplicates(test_2))
print(containsDuplicates(test_3))