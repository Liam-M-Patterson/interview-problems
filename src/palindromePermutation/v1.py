def isPalindromePermutation(string):
    dict = {}
    foundPivot = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isalpha():
            
            if( ch in dict and dict[ch] == 1):
                dict[ch] = 0
                foundPivot -= 1
            else:
                foundPivot += 1
                dict[ch] = 1
    
    return foundPivot <= 1

print(isPalindromePermutation("racecar"))
print(isPalindromePermutation("acerrac"))
print(isPalindromePermutation("liam"))
print(isPalindromePermutation("racecar!-"))
print(isPalindromePermutation("poo"))
print(isPalindromePermutation("santnas"))
