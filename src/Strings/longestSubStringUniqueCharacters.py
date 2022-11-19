def findSubString(s):
    if s == "":
        return 0
    
    # use l and r to define a window
    l = 0
    r = 0
    positions = {}
    length = 0
    while r < len(s):
        print('positions: ', positions)
        print(s[l:r], l, r)
        print('char:', s[r])
        if s[r] in positions:
            
            
            l = positions[s[r]] + 1
            r = l
            if r < len(s):
                positions[s[r]] = r
            print( "in positions:", l)
        else:
            length = max(length, r-l)
            # l = positions[s[r]] + 1
            r += 1
        
            positions[s[r]] = r
       
    return length+1

print(findSubString("aaacbabcdaa"))
# print(findSubString("a"))
# print(findSubString(""))
# print(findSubString("aaaaaaaaaaaaddddddddaaaadbaaaaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddd"))
            