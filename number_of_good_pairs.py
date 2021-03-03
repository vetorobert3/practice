def numIdenticalPairs(nums):
    l = {}
    count = 0

    # We are going to iterate through the list to see if elements in nums if elements repeat in the new dict, l.
    for num in nums: 
        if num not in l:
            # if not, then add num to dict with a 0 value
            l[num] = 0
        # increment the value in the dict + 1
        l[num] += 1

    # now we iterate through the l dict
    for num in l:
        # we now grab the value of the key: value pair
        n = l[num]
        count += (n*(n-1) // 2) # used to find the sum of n-1 numbers
        
    return count


numbers = [1,2,3,1,1,3]

print(numIdenticalPairs(numbers))