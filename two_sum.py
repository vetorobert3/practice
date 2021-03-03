"""
Understand:
    input: nums = [1,3,4], target = 7
    output: [1,2]

    input: nums = [1,2,4,6], target = 8
    output: [1,3]

Plan:
    Make a dict. Store the numbers in that dict that are NOT subtracted by the 
    target and the current position of i 
"""

def twoSum(nums, target):
    req = {}

    for i in range(len(nums)):
        if target - nums[i] in req: # this is subtracting current i from target to find the value needed to need to get the sum of target
            return [req[target - nums[i]], i] # if that value is found, this will return the index of the if statement by finding the value and also the index of the current i
        else:
            req[nums[i]] = i # this will make the nums[i] the key and the index will be the value in the dict

list = [6,2,1,1,9,4,3]

print(twoSum(list, 11))