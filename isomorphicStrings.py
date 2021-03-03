def csIsomorphicStrings(a, b):
    dictA = {}
    dictB = {}
    
    for i, value in enumerate(a):
        dictA[value] = dictA.get(value, []) + [i]
        
    for j, value in enumerate(b):
        dictB[value] = dictB.get(value, []) + [j]
        
    if sorted(dictA.values()) == sorted(dictB.values()):
        return True
    else:
        return False

a = 'egg'
b = 'odd'

print(csIsomorphicStrings(a, b))