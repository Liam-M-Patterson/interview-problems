def countSpaces(string, startPos, endPos):
    numSpaces = 0
    for i in range(endPos - startPos + 1):
        if string[i+startPos] == ' ':
            numSpaces += 1
    return numSpaces

def URLify(string, trueLength):
    if(len(string) == trueLength):
         return string
    if(string.count(' ') % 2 == 1):
        return("the string is not formatted correctly, check the number of spaces")
    string = list(string)

    numShifts = len(string) - trueLength
    print("num shifts: " + str(numShifts))
    i = trueLength -1
 
    while(i >= 0):
       # print("I: " + str(i))
        #print(string)
        #print("remaining spaces:" +str(numShifts/2))
        if numShifts/2 == 0:
         #   print("no more spaces")
            result = "".join(string)
            return result
        elif string[i] != ' ':
            string[i+numShifts] = string[i]
        elif (numShifts/2) > 0:
            string[i + numShifts] = '0'
            string[i + numShifts - 1] = '2'
            string[i + numShifts - 2] = '%'
            numShifts -= 2
        
        i -= 1
    
# print(countSpaces("  h  ", 2, 3))
# print(countSpaces("  h  ", 1, 4))
# print(countSpaces("  h  ", 2, 4))
print(URLify("liam", 4))
print(URLify("liam ", 4))
print(URLify("liam g  ", 6))
