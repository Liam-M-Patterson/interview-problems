class Solution:
    def numberOfWeakCharacters(self, properties):       

        #helper function to get the max def stat given an array
        def getMaxDef(arr):    
            MAX = 0
            for stats in arr:
                if stats[1] > MAX:
                    MAX = stats[1]
            return MAX
        
        #Sort based on attack value
        properties.sort(key=  lambda i: i[0])
        
        groups = {}
        highestAttack = 0
        numWeak = 0                
        

        for character in properties:
            
            highestAttack = max(highestAttack, character[0])
            
            #make a hashMap of groups of characters based on attack value
            if character[0] in groups:
                groups[character[0]].append(character)
            else:
                groups[character[0]] = [character]
        
        #get the maxDef from the highestAttack group
        maxDef = getMaxDef(groups[highestAttack])
        #since all charcaters with the highest attack cannot be weak, remove them
        del groups[highestAttack]
        
        #iterate through the groups going from strongest to weakest
        for group in reversed(groups):
            
            #check each character if they are weaker than the current maxDef
            #we already know that they are weaker based on attack, since we are going from strongest to weakest
            for character in groups[group]:
                if character[1] < maxDef:
                    numWeak += 1
            
            #update the maxDef stat
            maxDef = max(getMaxDef(groups[group]), maxDef)
            
        return numWeak
            