def isPalindromePermutation(string):
    dict = {}
    foundPivot = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if( string[i] in dict and dict[i]):
                dict[i] = 0
                foundPivot -= 1
            else:
                foundPivot += 1
                dict[i] = 1
    return foundPivot <= 1

print(isPalindromePermutation("racecar"))
print(isPalindromePermutation("acerrac"))
print(isPalindromePermutation("liam"))