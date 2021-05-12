def isUnique(string):
    dict = {}
    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    for freq in dict.values():
        if freq > 1:
            return False
    return True

def prettyPrint(string):
    print("String: " + string + " " + str(isUnique(string)))

prettyPrint("Liam")
prettyPrint("aaa")
prettyPrint("  ")