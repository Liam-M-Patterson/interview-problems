from collections import Counter

class Solution:
    def findOriginalArray(self, changed):
        
        """
        #tally occurrences of each number
        count = {}
        for num in changed:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        """
        count = Counter(changed) #more pythonic approach

        original = []
        #need to sort first, so that the original number will get used in the case of a double also being in the original
        # ex [4, 2, 8, 16 ...] if we do not sort, then the 4 will act as the original value to 8, when it shouldn't
        changed.sort()
        
        for num in changed:
            
            #if there is both the original and doubled value
            if num in count and 2*num in count:
                #decrement occurences 
                count[num] -= 1
                count[2*num] -= 1
                
                #if all occurences are "used", then remove
                if count[num] == 0:
                    del count[num]
                    
                #in the case num is 0, then it may have already been deleted with the above line
                if 2*num in count and count[2*num] == 0:
                    del count[2*num]

                #append num to result array
                original.append(num)
                    
        #if the hashMap still has remaining numbers, then that number was neither an original number or a double,
        # therefore the array is not a doubled array  
        if len(count) == 0:
            return original
        else:
            return []