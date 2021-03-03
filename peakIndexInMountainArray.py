def peakIndexInMountainArray(arr):
    # Like in any binery search, you first want to set up 
    # you min and max.
    min = 0
    max = len(arr) - 1

    # Here we set up a while loop. Another requirement
    # for a binary search    
    while min < max:
        # In the while loop, we set up the mid point
        mid = (min + max) // 2
            
        # here we set up the conditional
        if arr[mid] < arr[mid + 1]:
            min = mid + 1
        else:
            max = mid
                
    return min


    # lo, hi = 0, len(arr) - 1
    # while lo < hi:
    #     mi = (lo + hi) // 2
    #     if arr[mi] < arr[mi + 1]:
    #         lo = mi + 1
    #     else:
    #         hi = mi
    # return lo

nums = [24,69,100,99,79,78,67,36,26,19]
print(peakIndexInMountainArray(nums))