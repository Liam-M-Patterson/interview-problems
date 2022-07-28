import sys

def printPerms(s) :
    result = set()
    map = buildFreqTable(s)
    addPerms(map, '', len(s), result)
    return result

def buildFreqTable(s):
    map = {}
    for c in s:
        if c not in map:
            map[c] = 0
        map[c] = map.get(c) + 1
    return map

def addPerms(map, prefix, remaining, res):

    if remaining == 0:
        res.add(prefix)
        return
    
    for c in map:
        count = map.get(c)
        if count > 0:
            map[c] = count - 1
            addPerms(map, prefix+c, remaining-1, res)
            map[c] = count


if __name__ == "__main__":
    
    perms = printPerms(sys.argv[1])
    print(perms)