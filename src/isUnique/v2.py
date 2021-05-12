import re
def isUnique(string):
    temp = sortedString = sorted(string)
    for char in temp:
        temp = re.sub(char + '+', char, temp)
    return temp == sortedString

#print(re.sub('a+', 'a', "aa"))
print(str(isUnique("liam")))
print(str(isUnique("aaa")))