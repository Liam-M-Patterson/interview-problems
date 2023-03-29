def checkPermutation(s1, s2):
    return sorted(s1) == sorted(s2)

print(str(checkPermutation("hello", "elloh")))
print(str(checkPermutation("hello", "ello32h")))
print(str(checkPermutation("hello", "elLoh")))