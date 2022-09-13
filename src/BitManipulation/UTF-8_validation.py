class Solution:
    def validUtf8(self, data):
        
        i = 0
        while i < len(data):

            byte = data[i]
            continuations = 0
            
            #check if 1 byte pattern shift so xxxx xxx0
            if (byte >> 7)  == 0:
                i += 1
            #check if 2 byte pattern shift so xxxx x110
            elif (byte >> 5) & 255 == 6:
                continuations = 1
                i += 1
            #check if 3 byte pattern shift so xxxx 1110
            elif (byte >> 4) & 255 == 14:
                continuations = 2
                i += 1
            #check if 4 byte pattern shift so xxx1 1110
            elif (byte >> 3) & 255 == 30:
                continuations = 3
                i += 1
            else:
                return False
                
            #loop through additonal continuations
            while continuations > 0 and i < len(data):
                
                #shift so byte is xxxx xx10
                if ( (data[i] >> 6) & 2) == 2:
                    i += 1
                    continuations -= 1
                else: 
                    return False

            #if reached the end of the array and there are continuations remaining, not a valid UTF-8 Encoding                    
            if continuations > 0: return False
        #if reached the end of the input array, then it was valid
        return True