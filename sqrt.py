def mySqrt(x):
    min, max = 0, x
    res = 0

    while min <= max:
        mid = (min + max) // 2
        squared = mid * mid

        if squared == x:
            return mid
        elif squared > x:
            max = mid - 1
        else:
            min = mid + 1
            res = mid
    return res

root = 16
print(mySqrt(root))