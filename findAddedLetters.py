def csFindAddedLetter(str_1, str_2):
    letters = {}
        
    for i in str_2:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
            
    for i in str_1:
        letters[i] -= 1
        
    for j in letters:
        if letters[j] == 1:
            return j

str1 = "bcde"
str2 = "bcdef"

print(csFindAddedLetter(str1, str2))