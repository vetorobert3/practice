"""
Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order
"""

def csGroupAnagrams(strs):
    res = {}
    
    for i in strs:
        s = "".join(sorted(i))
        if s in res:
            res[s].append(i)
        else:
            res[s] = [i]
    return list(res.values())

strs = ["apt","pat","ear","tap","are","arm"]

print(csGroupAnagrams(strs))